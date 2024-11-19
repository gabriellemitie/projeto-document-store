# projeto-document-store  
## Alunas  

Aléxia Santa Rosa Suares  RA:  22.224.016-0     
Gabrielle Mitie Suzuke Tenguan   RA: 22.124.097-1  
Larissa Gonçalves da Silva   RA: 22.224.022-8    


## Como rodar o projeto  
1. Rodar arquivo 'hefesto' para criação das tabelas no pgadmin
2. Rodar arquivo 'main.py' para poder popular as tabelas
3. Rodar arquivo 'teste.py' para poder fazer a conversão das tabelas de postgres para formato MongoDb
4. Rodas queries na pasta 'Queries'
5. Caso precise deletar todas as tabelas no postgres, usar 'hades.sql'  



## Descrição das coleções usadas para armazenar os dados  
```json
- Coleção Aluno
  {
  RA: <int>
  nome_aluno: <varchar>
  ano_matricula: <int>
  curso: <object> --> vem da coleção Curso
    id_curso: <objectID> --> coleção Curso
    nome_curso: <varchar>
  disciplinas: <array> --> vem da coleção Disciplina; é um array de objetos, ou seja, várias disciplinas
  object
    codigo_disc: <objectID> --> coleção Disciplina
    nome_disc: <varchar>
    ano_disc: <int>
    codigo_prof: <varchar>
  id_tcc: <int>
  historico_escolar: <array> --> retorna array de objetos
    object 
      nota: <numeric>
      semestre_cursado: <int>
      ano_cursado: <int>
  matriz_curricular: <array> --> array de objetos
    object
      id_matriz: <varchar>
      semestre_aprovado: <int>
      ano_aprovado: <int>
  }


  - Coleção HistoricoEsc
  {
  nota: <numeric>
  semestre_cursado: <int>
  ano_cursado: <int>  
  RA: <objectID>
  codigo_disc: <objectID> --> coleçõ Disciplina
  }

  - Coleção HistoricoDisc
  {
  ano_ministrado: <int>
  semestre_ministrado: <int>
  codigo_prof: <objectID>  --> coleção Professor
  codigo_disc: <objectID> --> coleção Disciplina
  }


- Coleção Disciplinas
  {
  codigo_disc: <varchar>
  nome_disc: <varchar>
  ano_disc: <int>
  semestre_disc: <int>
  codigo_prof: <objectID> --> coleção Professor 
  id_curso: <objectID>  --> coleção Curso
  
  }

  - Coleção MatrizCurricular
  {
  id_matriz: <int>
  semestre_aprovado: <int>
  ano_aprovado: <int>  
  id_curso: <objectID> --> coleção Curso
  codigo_disc: <objectID> --> coleção Disciplina
  }
  

  - Coleção Formados
  {
  RA: <objectID>  --> coleção Aluno
  id_matriz: <objectID> --> coleção matrizcurricular
  }


- Coleção Departameneto
  {
  nome_dep: <varchar>
  codigo_dep: <varchar>
  codigo_prof: <objectID> --> coleção Professor
  codigo_disc: <objectID> --> coleção Disciplina
  id_curso: <objectID>   --> coleção Curso
  }


    - Coleção Professor
  {
  codigo_prof: <int>  
  nome_prof: <varchar>
  chefe_dep: <boolean>
  id_curso: <objectID> --> coleção Curso
  id_tcc: <objectID> --> coleção TCC
  departamento: <object> --> coleção Departamento
    nome_dep: <varchar>
  disciplinas: <array> --> array de objetos
    codigo: <varchar>
    nome: <varchar>
  historico_disciplinas: <array>
    codigo_disc: <varchar>
    nome_disc: <varchar>
    semestre_ministrado: <int>
    ano_ministrado: <int>
 }


  - Coleção TCC
  {
  id_tcc: <int>
  RA: <objectID> --> coleção Aluno
  }

 - Coleção curso
  {
  id_curso: <int>
  nome_curso: <varchar>
  departamento: <object> -> vem da coleção Departamento
    codigo_dep: <varchar>
    nome_dep: <varchar>  
  disciplinas: <array> --> coleção Disciplinas; array de objetos
    object
      codigo_disc: <varchar>
      nome_disc: <varchar>
      ano_disc: <int>
      codigo_prof: <varchar>
  matriz_curricular: <array> --> array de objetos
    objeto
      id_matriz: <varchar>
      semestre_aprovado: <int>
      ano_aprovado: <int>
  professores: <array> --> array de objetos
    object
      codigo_prof: <varchar>
      nome_prof: <varchar>
  }
```

## Exemplo coleções

### Aluno
![image](https://github.com/user-attachments/assets/a9be7e33-4f73-446f-be77-c530d38991cf)  

### Curso  

![image](https://github.com/user-attachments/assets/d0533ce2-22ba-4602-b2a4-3049b647a4c8)  

### Professor  
![image](https://github.com/user-attachments/assets/50cdc1e7-f173-451d-81e9-83b9a19b1a39)

















 
