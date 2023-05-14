import React, { useEffect, useState } from "react";
import axios from "axios";
import { useHistory } from "react-router-dom";
import prevbtn from "../img/prevbtn.png";
import styles from "./TestCompletedPage.module.css";

const TestCompletedPage = () => {
    const [userMBTI, setUserMBTI] = useState("")

    const history = useHistory();

    useEffect(() => {
        async function getMBTI() {
            try {
                const res = await axios.get("http://localhost:5000/result/", {withCredentials: true})
                setUserMBTI(res.data.user_mbti)
            } catch (error) {
                console.log(error)
            }
        }
        getMBTI();
    }, [userMBTI]);
    
    return (
        <div id={styles.container}>
            <div id={styles.btnbox} onClick={ () => { history.goBack() }}>
                <img className={styles.prevbtn} src={prevbtn} alt="prevbtn" />
            </div>

            <div className={styles.title}>
                <p>일리스</p>
            </div>

            <div id={styles.divider}></div>

            <div>
                <p className={styles.text}>테스트가 완료되었습니다</p>
            </div>
            
            <div>
                <button className={styles.btn1} onClick={ () => { history.push("/MbtiCharacterPage") }}>나와 같은 유형인 <br /> 캐릭터 확인하기</button>
            </div>

            <div>
                <button className={styles.btn2} onClick={ () => { history.push("/MbtiCompatiblePage") }}>나와 궁합이 잘 맞는 <br /> 캐릭터 확인하기</button>
            </div>

            <div>
                <button className={styles.btn3} onClick={ () => { history.push("/MbtiTop10Page") }}>{userMBTI} 유형 관련 인기있는 <br /> 영화 확인하기</button>
            </div>
        </div>
    )
}

export default TestCompletedPage;