import React, { useState } from "react";
import styles from "./MainPage.module.css";
import Modal from "../components/Modal";
import LoginModal from "../components/LoginModal"

const MainPage = () => {
    const [showModal, setShowModal] = useState(false);
    const [showLoginModal, setShowLoginModal] = useState(false);

    const openModal = () => {
        setShowModal(!showModal);
    }

    const openLoginModal = () => {
        setShowLoginModal(!showLoginModal);
    }

    return (
        <div id={styles.container}>
            <div className={styles.title}>
                <div>일리스</div>
            </div>

            <div id={styles.divider}></div>

            <div id={styles.img} className={styles.imgwrapper}>
                <img className={styles.contentimg} src="img/for_test/0.png" alt="main logo" />
            </div>

            <div>
                <div id={styles.maintext1}>코로나 시국에..</div>
                <div id={styles.maintext2}>이런게 나의 영화 인생캐 일리가...!!</div>
            </div>
            
            <div className={styles.btn_container}>
                <div>
                    <button id={styles.leftbtn} onClick={ openLoginModal }>인생캐 알아보기</button>
                    { showLoginModal && <LoginModal openLoginModal={openLoginModal} />}
                </div>

                <div>
                    <button id={styles.rightbtn} onClick={openModal}>바로 결과 보기</button>
                    { showModal && <Modal openModal={openModal} />}
                </div>
            </div>
        </div>
    )
}

export default MainPage;