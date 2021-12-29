UPDATE filmes 
SET nome = <dtml-sqlvar nome type=nb>,
	elenco = <dtml-sqlvar elenco type=nb>,
	categoria_id = <dtml-sqlvar categoria_id type=int>,
	imgurl = <dtml-sqlvar imgurl type=nb>,
	sinopse = <dtml-sqlvar sinopse type=nb>
WHERE cod_id = <dtml-sqlvar cod_id type=int>