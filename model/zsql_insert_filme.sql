INSERT INTO filmes (nome, elenco, categoria_id, sinopse, imgurl) VALUES
(
	<dtml-sqlvar nome type=nb>,
	<dtml-sqlvar elenco type=nb>,
	<dtml-sqlvar categoria_id type=int>,
	<dtml-sqlvar sinopse type=nb>,
	<dtml-sqlvar imgurl type=nb>
)
