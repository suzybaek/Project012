import React, { useEffect, useState } from "react";
import axios from "axios";
import styles from "./MovieInfoModal.module.css";
import closebtn from "../img/closebtn.png";
import send from "../img/send.png";
import { FaStar } from "react-icons/fa";

const colors = {
    orange: "#FFBA5A",
    grey: "#a9a9a9"
}

const MovieInfoModal = ({ openModal, selectedMovie }) => {
    const [curValue, setCurValue] = useState(0);
    const [hoverValue, setHoverValue] = useState(undefined);
    const [satisfactionList, setSatisfactionList] = useState([]);

    const [movieId, setMovieId] = useState("");
    const [rating, setRating] = useState("");

    const stars = Array(5).fill(0);

    let axiosConfig = {
        headers: {
            'Content-Type': 'application/json;charset=UTF-8',
            // "Access-Control-Allow-Origin": "*",
        },
        withCredentials: true
    }

    const handleClick = (value) => {
        setCurValue(value)
        setMovieId(selectedMovie.id)
        setRating(value * 2)

        let list = [...satisfactionList]
        list = [[
            movieId,
            rating
            ]]
        setSatisfactionList(list)

        return satisfactionList;
    };

    useEffect(() => {
        let list = [...satisfactionList]
        list = [[
            movieId,
            rating
            ]]
        setSatisfactionList(list)
    }, [movieId, rating])

    const handleMouseOver = (value) => {
        setHoverValue(value)
    };
    
    const handleMouseLeave = () => {
        setHoverValue(undefined)
    };

    const sendReview = () => {
        axios
            .post("http://localhost:5000/character/movie_list", {
                "satisfaction_list": satisfactionList
            }, axiosConfig)
            .then(() => {
            })
            .catch((error) => {
                console.log(error)
            })
    }

    return (
        <div className={styles.modal_container}>
            <div className={styles.modal}>
                <img src={closebtn} alt="closebtn" onClick={ openModal } className={styles.modal_button} />
                <img className={styles.modal_img} src={selectedMovie.image_link} alt={selectedMovie.kor_title + " 포스터"}/>
                <div className={styles.modal_movie_info_container}>
                    <p>감독 : {selectedMovie.director}</p>
                    <p>장르 : {selectedMovie.genres[0]}</p>
                    <p>제목 : {selectedMovie.kor_title}</p>
                    <p>개봉년도 : {selectedMovie.pub_year}년</p>
                    <p>평점 : {selectedMovie.rating}점</p>
                    <p>러닝타임 : {selectedMovie.run_time}분</p>
                </div>
                <div className={styles.modal_movie_story_container}>
                    <p>{selectedMovie.story.substring(0, 500)+"..."}</p>
                </div>
                <div className={styles.RatingContainer}>
                    <div className={styles.stars}>
                        {stars.map((_, index) => {
                            return (
                                <FaStar 
                                    key={index}
                                    size={48}
                                    style={{
                                        marginRight: 10,
                                        cursor: "pointer"
                                    }}
                                    color={ (hoverValue || curValue) > index ? colors.orange : colors.grey }
                                    onClick={ () => handleClick(index + 1) }
                                    onMouseOver={ () => handleMouseOver(index + 1) }
                                    onMouseLeave={ handleMouseLeave }
                                    
                                />
                            )
                        })}
                        <img className={styles.modal_rating_send} src={send} alt="ratingsend" onClick={ sendReview } />
                    </div>
                </div>
            </div>
        </div>
    )
}

export default MovieInfoModal;