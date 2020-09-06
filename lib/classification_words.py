import nltk
import pandas as pd


class root_classify_words():

    def keywords_inventory(self, dataframe, colonne='Description'):
        is_noun = lambda pos: pos[:2] == 'NN'  # 名词开头标记为NN

        stemmer = nltk.stem.SnowballStemmer("english")
        keywords_roots = dict()  # collect the words / root
        keywords_select = dict()  # association: root <-> keyword
        category_keys = []
        count_keywords = dict()
        for s in dataframe[colonne]:
            if pd.isnull(s): continue
            lines = s.lower()
            tokenized = nltk.word_tokenize(lines)
            nouns = [word for (word, pos) in nltk.pos_tag(tokenized) if is_noun(pos)]

            for t in nouns:
                t = t.lower()
                racine = stemmer.stem(t)
                if racine in keywords_roots:
                    keywords_roots[racine].add(t)
                    count_keywords[racine] += 1
                else:
                    keywords_roots[racine] = {t}
                    count_keywords[racine] = 1

        for s in keywords_roots.keys():
            if len(keywords_roots[s]) > 1:
                # 如果对应root的value多于一个words，选长度最小的word代表这个root
                min_length = 1000
                for k in keywords_roots[s]:
                    if len(k) < min_length:
                        clef = k
                        min_length = len(k)
                category_keys.append(clef)
                keywords_select[s] = clef
            else:
                # 如果对应root的value只有一个words
                category_keys.append(list(keywords_roots[s])[0])
                keywords_select[s] = list(keywords_roots[s])[0]

        print("Number of keywords in variable '{}': {}".format(colonne, len(category_keys)))
        return category_keys, keywords_roots, keywords_select, count_keywords

