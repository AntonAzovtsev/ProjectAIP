import sqlite3

class BotDB:

    def __init__(self, db_file):
        """Инициализация соединения с БД"""
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()
    def get_recipe_id(self, ingredient):
        """"Нахождение id нужного рецепта"""
        result = self.cursor.execute("SELECT `id` FROM `recipes` WHERE `ingredient` = ?", (ingredient,))
        return result.fetchone()
    def get_recipe(self, ingredient):
        """Нахождение нужных рецепта"""
        result = self.cursor.execute("SELECT * FROM `recipes` WHERE `ingredient` = ?",
                                     (ingredient,))

        return result.fetchall()
    def add_record(self, recipe_id, review):
        """Добавление отзыва от пользователя"""
        self.cursor.execute("INSERT INTO `reviews` (`recipe_id`, `review`) VALUES (?, ?)",
                            (recipe_id,
                             review))
        return self.conn.commit()

    def close(self):
        """Закрытие соединения"""
        self.conn.close()