create schema ouvidoria_projeto_abella;

use ouvidoria_projeto_abella;

create table manifestacoes(
    codigo int auto_increment,
    descricao varchar(3000),
    categoria varchar(10),
    autor varchar(50),
    primary key (codigo)
);

insert into manifestacoes (descricao, categoria, autor) values
('Internet muito lenta','Reclamaçao','Ingrid Reis'),
('Ultimas ofertas da black friday foram otimas','Elogio','Herbert Richards'),
('Voces deveriam melhorar o atendimento chat no whatsapp','Sugestao','Yuri Rafael');

select * from manifestacoes;
