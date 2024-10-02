# projeto-document-store  
## Alunas  

Aléxia Santa Rosa Suares  RA:   
Gabrielle Mitie Suzuke Tenguan   RA: 22.124.097-1  
Larissa Gonçalves da Silva   RA: 22.222.  




## Descrição das coleções usadas para armazenar os dados  

- Coleção Aluno
  {
  RA: <int>
  nome_aluno: <varchar>
  ano_matricula: <int>  
  id_curso: <objectID>
  codigo_disc: <objectID>
  id_tcc: <int>
  }


  - Coleção HistoricoEsc
  {
  nota: <numeric>
  semestre_cursado: <int>
  ano_cursado: <int>  
  RA: <objectID>
  codigo_disc: <objectID>
  }

  - Coleção HistoricoDisc
  {
  ano_ministrado: <int>
  semestre_ministrado: <int>
  codigo_prof: <objectID>  
  codigo_disc: <objectID>
  }


- Coleção Disciplinas
  {
  codigo_disc: <varchar>
  nome_disc: <varchar>
  ano_disc: <int>
  semestre_disc: <int>
  codigo_prof: <objectID>
  id_curso: <objectID>  
  
  }

  - Coleção MatrizCurricular
  {
  id_matriz: <int>
  semestre_aprovado: <int>
  ano_aprovado: <int>  
  id_curso: <objectID>
  codigo_disc: <objectID>
  }
  

  - Coleção Formados
  {
  RA: <objectID>
  id_matriz: <objectID>
  }


- Coleção Departameneto
  {
  nome_dep: <varchar>
  codigo_dep: <varchar>
  codigo_prof: <objectID>
  codigo_disc: <objectID>
  id_curso: <objectID>   
  }


    - Coleção Professor
  {
  codigo_prof: <int>  
  nome_prof: <varchar>
  chefe_dep: <boolean>
  id_curso: <objectID>
  id_tcc: <objectID>
 }


  - Coleção TCC
  {
  id_tcc: <int>
  RA: <objectID>
  }


   - Coleção curso
  {
  id_curso: <int>
  nome_curso: <varchar>
  }
















 
