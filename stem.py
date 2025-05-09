def stem(self, word: str):
        list_item = self.__processing(self.__clean_word(word))
        #print(list_item)
        # return str([d['stem'] for d in list_item])

        # return list_item[0]['stem']    # dict['stem] == dict.get('stem')
        return list_item[0]['stem']