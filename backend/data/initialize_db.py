from app import db

def init_db():
    # 데이터베이스 초기화. 현재는 데이터 적재되어 있음. 필요한 경우 실행.
    from .store_data import store_init_data
    db.create_all()
    store_init_data()

    from .store_movie_data import store_movie_json, store_chracter_image, set_to_default_char_image
    store_movie_json()
    store_chracter_image()
    set_to_default_char_image()

    from .refine_data import delete_null_image_in_DB, delete_html_entity
    delete_null_image_in_DB()
    delete_html_entity()