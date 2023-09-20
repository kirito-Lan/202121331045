from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
from scipy.linalg import norm


def tf_similarity(s1, s2):
    def add_space(s):
        return ' '.join(list(s))

    s1, s2 = add_space(s1), add_space(s2)  # 在字中间加上空格
    cv = CountVectorizer(tokenizer=lambda s: s.split())  # 转化为TF矩阵
    corpus = [s1, s2]
    vectors = cv.fit_transform(corpus).toarray()  # 计算TF系数
    return np.dot(vectors[0], vectors[1]) / (norm(vectors[0]) * norm(vectors[1]))


# s1 = '今天是周天，天气晴朗，我晚上要去看电影啊啊啊.开挖掘机,我靠'
# s2 = '今天是周天，天气晴朗，我晚上要去看电影.阿里阿里巴巴'
# print(tf_similarity(s1, s2))

if __name__ == '__main__':
    import SRC
    SRC.get_addr()
