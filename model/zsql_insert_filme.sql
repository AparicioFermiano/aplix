INSERT INTO filmes (nome, elenco, cod_categoria, sinopse, imgurl) VALUES
(
	<dtml-sqlvar nome type=nb>,
	<dtml-sqlvar elenco type=nb>,
	<dtml-sqlvar cod_categoria type=int>,
	<dtml-sqlvar sinopse type=nb>,
	<dtml-sqlvar imgurl type=nb>
)
