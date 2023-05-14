import React, { useEffect, useState } from "react";
import axios from "axios";
import { useHistory } from "react-router-dom";
import prevbtn from "../img/prevbtn.png";
import home from "../img/home.png";
import Top10MovieInfoModal from "../components/Top10MovieInfoModal";
import styles from "./MbtiTop10Page.module.css";


const MbtiTop10Page = () => {
    const [top10, setTop10] = useState([]);
    const [selectedMovie, setSelectedMovie] = useState([]);

    const [showModal, setShowModal] = useState(false);

    const history = useHistory();

    const openModal = () => {
        setShowModal(!showModal);
    }

    useEffect(() => {
        async function getTop10() {
            try {
                const res = await axios.get("http://localhost:5000/result/top10", {withCredentials: true})
                setTop10(res.data)
            } catch (error) {
                console.log(error)
            }
        }
        getTop10();
    }, []);

    const clickHandler = (item) => {
        setSelectedMovie(item);
        openModal();
    }

    const logout = () => {
        axios
            .get("http://localhost:5000/user/logout", {withCredentials: true})
            .then(() => {
                history.push("/")
            })
            .catch((error) => {
                console.log(error)
            })
    }
    
    return (
        <div id={styles.container}>
            <div id={styles.btnbox} onClick={  () => { history.goBack() } }>
                <img className={styles.prevbtn} src={ prevbtn } alt="prevbtn" />
            </div>

            <div className={styles.title}>
                <p>일리스</p>
            </div>

            <div id={styles.divider}></div>

            <div>
                <p className={styles.char_name}>네이버 인기있는 영화 TOP 10 워드 클라우드</p>
                <img className={styles.word_cloud} src={ top10.word_cloud_src } alt={ top10.word_cloud_src } />
            </div>

            <div>
                <p className={styles.char_name}>네이버 인기있는 영화 TOP 10</p>
                <div className={styles.charlist}>
                { top10.top10_in_naver && top10.top10_in_naver.map((item, idx) => {
                    return (
                        <div key={ idx }>
                            <img className={styles.char_img} src={ item[3] } alt={ item[1] + " 포스터" }  onClick={ () => clickHandler(item) } />
                            { showModal && <Top10MovieInfoModal openModal={openModal} selectedMovie={selectedMovie} />}
                            <p className={styles.movie_name}>{ item[1] }</p>
                        </div>
                    )
                }) }
                </div>
            </div>

            <div>
                <p className={styles.char_name}>같은 유형에게 인기있는 영화 TOP 10</p>
                <div className={styles.charlist}>
                { top10.top10_for_same_mbti_users && top10.top10_for_same_mbti_users.map((item, idx) => {
                    return (
                        <div key={ idx }>
                            <img className={styles.char_img} src={ item[3] } alt={ item[1] + " 포스터" }  onClick={ () => clickHandler(item) } />
                            { showModal && <Top10MovieInfoModal openModal={openModal} selectedMovie={selectedMovie} />}
                            <p className={styles.movie_name}>{ item[1] }</p>
                        </div>
                    )
                }) }
                </div>
            </div>

            <div>
                <img className={styles.homebtn} src={ home } alt="home button" onClick={ logout } />
            </div>
        </div>
    )
}

export default MbtiTop10Page;