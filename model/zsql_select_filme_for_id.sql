SELECT * FROM filmes 
INNER JOIN categoria ON categoria.cod_categoria = filmes.categoria_id
where
cod_id=<dtml-sqlvar cod_id type=int>

