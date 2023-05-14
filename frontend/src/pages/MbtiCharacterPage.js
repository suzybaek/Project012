import React, { useEffect, useState } from "react";
import axios from "axios";
import { useHistory } from "react-router-dom";
import prevbtn from "../img/prevbtn.png";
import refreshbtn from "../img/refresh.png";
import styles from "./MbtiCharacterPage.module.css";


const MbtiCharacterPage = () => {
    const [userMBTI, setUserMBTI] = useState("");
    const [charList, setCharList] = useState([]);

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
        async function getMbtiCharacter() {
            try {
                const res = await axios.get("http://localhost:5000/character/0", {withCredentials: true})
                setCharList(res.data.character_info)
            } catch (error) {
                console.log(error)
            }
        }
        getMbtiCharacter();
    }, [userMBTI]);

    const refreshHandler = () => {
        async function getMbtiCharacterRefresh() {
            try {
                const res = await axios.get("http://localhost:5000/character/refresh/0", {withCredentials: true})
                setCharList(res.data.character_info)
            } catch (error) {
                console.log(error)
            }
        }
        getMbtiCharacterRefresh();
    }

    const clickHandler = (idx) => {
        history.push({
            pathname: "/MbtiCharacterMovieListPage",
            state: {
                idx : idx,
                charList : charList
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
                <p className={styles.text1}>나와 같은 유형의 영화 속 캐릭터</p>
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

export default MbtiCharacterPage;