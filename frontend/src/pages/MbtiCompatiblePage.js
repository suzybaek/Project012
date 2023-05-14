import React, { useEffect, useState } from "react";
import axios from "axios";
import { useHistory } from "react-router-dom";
import prevbtn from "../img/prevbtn.png";
import refreshbtn from "../img/refresh.png";
import styles from "./MbtiCompatiblePage.module.css";


const MbtiCompatiblePage = () => {
    const [userMBTI, setUserMBTI] = useState("");
    const [charList, setCharList] = useState([]);
    const [compatibleMBTI, setCompatibleMBTI] = useState("");

    const history = useHistory();

    useEffect(() => {
        async function getMbti() {
            try {
                const mbti = await axios.get("http://localhost:5000/result/", {withCredentials: true})
                setUserMBTI(mbti.data.user_mbti)
            } catch (error) {
                console.log(error)
            }
        }
        getMbti();
    }, [userMBTI]);

    
    useEffect(() => {
        async function getCompatibleCharacter() {
            try {
                const res = await axios.get("http://localhost:5000/character/1", {withCredentials: true})
                setCharList(res.data.character_info)
                setCompatibleMBTI(res.data.characters_mbti)
            } catch (error) {
                console.log(error)
            }
        }
        getCompatibleCharacter();
    }, [userMBTI]);

    const refreshHandler = () => {
        async function getMbtiCharacterRefresh() {
            try {
                const res = await axios.get("http://localhost:5000/character/refresh/1", {withCredentials: true})
                setCharList(res.data.character_info)
            } catch (error) {
                console.log(error)
            }
        }
        getMbtiCharacterRefresh();
    }

    const clickHandler = (idx) => {
        history.push({
            pathname: "/MbtiCompatibleMovieListPage",
            state: { 
                compatibleMBTI : compatibleMBTI,
                idx : idx 
            }
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
                <p className={styles.text1}>나와 궁합이 잘 맞는 캐릭터</p>
            </div>

            <div onClick={ refreshHandler }>
                <img className={styles.refreshbtn} src={ refreshbtn } alt="refreshbtn" />
            </div>

            <div>
                <p className={styles.text2}>맘에 드는 캐릭터를 클릭해 어떤 영화에 등장했는지 확인해 보세요</p>
            </div>

            <div>
                <div className={styles.charlist}>
                    { charList && charList.map((item, idx) => {
                        return (
                            <div key={ idx }>
                                <img className={styles.char_img} src={ item[2] } alt={ item[1] + " 사진" } onClick={ () => clickHandler(idx) } />
                                <p className={styles.char_name}>{ item[1] }</p>
                            </div>
                        )
                    }) }
                </div>
            </div>

        </div>
    )
}

export default MbtiCompatiblePage;