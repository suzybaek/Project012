import React, { useEffect, useState } from "react";
import axios from "axios";
import { useHistory } from "react-router-dom";
import prevbtn from "../img/prevbtn.png";
import styles from "./TestPage.module.css";


const TestPage = () => {
    const [index, setIndex] = useState(1);
    const [anslist, setAnsList] = useState([]);
    const [question, setQuestion] = useState([]);
    const [img, setImg] = useState([]);
    const [option, setOption] = useState([]);
    const QUESTION_EX_INDEX = 1;
    const QUESTION_LAST_INDEX = 13;

    const history = useHistory();

    let axiosConfig = {
        headers: {
            'Content-Type': 'application/json;charset=UTF-8',
            // "Access-Control-Allow-Origin": "*",
        },
        withCredentials: true
    }

    useEffect(() => {
        async function getQuestion() {
            try {
                const res = await axios.get(`http://localhost:5000/test/${index}`, {withCredentials: true})
                setQuestion(res.data.question);
                setImg(res.data.img_url)
                setOption(res.data.options);
            } catch (error) {
                console.log(error)
            }
        }
        getQuestion();
    }, [index]);

    const clickHandler = (e) => {
        if(index === QUESTION_LAST_INDEX) {
            const ans = [...anslist]
            ans.push(e.target.value)
            setAnsList(ans);
            axios.post("http://localhost:5000/result/", {
                "answers": [...anslist, e.target.value]
            }, axiosConfig)
            .then(() => {
                history.push("/TestCompletedPage")
            })
            .catch((error) => {
                console.log(error)
            })
            // const ans = [...anslist]
            // ans.push(e.target.value)
            // setAnsList(ans)
        } else if (index === QUESTION_EX_INDEX) {
            setIndex(index + 1)
        } else {
            const ans = [...anslist]
            ans.push(e.target.value)
            setAnsList(ans)
        }
        setIndex(index + 1)
    }
    
    const prevClick = () => {
        if(index === QUESTION_EX_INDEX) {
            history.goBack()
        } else {
            anslist.pop();
            setIndex(index - 1)
        }
    }

    return (
        <div id={styles.container}>
            <div id={styles.btnbox} onClick={prevClick}>
                <img className={styles.prevbtn} src={prevbtn} alt="prevbtn" />
            </div>

            <div className={styles.title}>
                <p>일리스</p>
            </div>

            <div id={styles.divider}></div>

            <div id={styles.img}>
                <img className={styles.contentimg} src={img} alt="main logo" />
            </div>

            <div id={styles.testtext}>
                <p>{question}</p>
            </div>

            {
                (index === QUESTION_EX_INDEX) ? 
                <div>
                    <div id={styles.progress}>
                        <div>1 / 12</div>
                    </div>
                    <div>
                        <button id={styles.ansA} onClick={clickHandler}>다음</button>
                    </div>
                </div> :
                <div>
                    <div id={styles.progress}>
                        <div>{index - 1} / 12</div>
                    </div>
                    <div>
                        <button id={styles.ansA} value="a" onClick={clickHandler}>{option[0]}</button>
                    </div>

                    <div>
                        <button id={styles.ansB} value="b" onClick={clickHandler}>{option[1]}</button>
                    </div>
                </div>
            }
        </div>
    )
}

export default TestPage;