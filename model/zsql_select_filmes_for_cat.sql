<dtml-if cod_categoria>
     select * from filmes
     where
     cod_categoria=<dtml-sqlvar cod_categoria type=int>
<dtml-else>
     select * from filmes
</dtml-if>
