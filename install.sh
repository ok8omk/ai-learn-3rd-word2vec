wget http://www.cl.ecei.tohoku.ac.jp/~m-suzuki/jawiki_vector/data/20170201.tar.bz2 -O word2vec/model.tar.bz2
tar -jxvf word2vec/model.tar.bz2 -C word2vec
rm word2vec/model.tar.bz2
mv word2vec/entity_vector/entity_vector.model.bin word2vec/models
rm -r word2vec/entity_vector
