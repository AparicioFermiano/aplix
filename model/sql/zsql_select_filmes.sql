<dtml-if nome>
     select * from filmes
     where
     nome ilike '<dtml-var nome>%'
<dtml-else>
     select * from filmes
</dtml-if>