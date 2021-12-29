<dtml-if categoria_id>
     select * from filmes
     where
     categoria_id=<dtml-sqlvar categoria_id type=int>
<dtml-else>
     select * from filmes
</dtml-if>
