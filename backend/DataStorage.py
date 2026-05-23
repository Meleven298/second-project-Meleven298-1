import json
import os


class DataStorage:
    '''Класс для сохранения и загрузки данных.'''
    
    @staticmethod
    def save(filename: str, data: dict) -> None:
        '''Сохраняет данные в JSON файл.
        
        Args:
            filename: Файл для сохранения.
            data: Данные для сохранения.
        '''
        
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    
    @staticmethod
    def load(filename: str, default: dict = None) -> dict:
        '''Загружает данные из JSON файла.
        
        Args:
            filename: Файл для выгрузки.
            default: В случае если не получится выгрузить данные.
        
        Returns:
            result: Данные в виде словаря либо ничего.
        '''

        result = default or {}
        
        if os.path.exists(filename):
            try:
                with open(filename, "r", encoding="utf-8") as f:
                    result = json.load(f)
            except:
                result = default or {}
        
        return result
    