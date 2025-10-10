CREATE DATABASE locadora;

USE locadora;
 
-- Criação da tabela diretor
CREATE TABLE diretor(

 id_diretor INT auto_increment primary key,

    nome VARCHAR(255),

    sobrenome VARCHAR(255),

    genero ENUM ("Feminino","Masculino","Outro")

);
 
INSERT INTO diretor (nome, sobrenome, genero) VALUES 

('João', 'Carvalho', 'Masculino'),

('Mariana', 'Silva', 'Feminino'),

('Carlos', 'Pereira', 'Masculino'),

('Ana', 'Souza', 'Feminino'),

('Rafael', 'Almeida', 'Masculino'),

('Beatriz', 'Oliveira', 'Feminino'),

('Lucas', 'Mendes', 'Outro'),

('Fernanda', 'Costa', 'Feminino'),

('Eduardo', 'Lima', 'Masculino'),

('Juliana', 'Ferreira', 'Feminino'),

('André', 'Rodrigues', 'Masculino'),

('Patrícia', 'Martins', 'Outro'),

('Vinícius', 'Gonçalves', 'Masculino'),

('Camila', 'Araújo', 'Feminino'),

('Gustavo', 'Ribeiro', 'Masculino'),

('Larissa', 'Barbosa', 'Feminino'),

('Diego', 'Nascimento', 'Masculino'),

('Sofia', 'Teixeira', 'Feminino'),

('Felipe', 'Moura', 'Masculino'),

('Alex', 'Torres', 'Outro');
 
SELECT * FROM Diretor;
 
-- Criação da tabela Filme

CREATE TABLE filme(

 id_filme INT AUTO_INCREMENT PRIMARY KEY,

    titulo VARCHAR (255) NOT NULL,

    atores VARCHAR(255) NOT NULL,

    diretor VARCHAR(255) NOT NULL,

    ano YEAR NOT NULL,

    genero VARCHAR(255) NOT NULL,

    produtora VARCHAR(255) NOT NULL,

    sinopse TEXT NOT NULL

);
 
INSERT INTO filme (titulo, atores, diretor, ano, genero, produtora, sinopse) VALUES

('The Exorcist', 'Ellen Burstyn', 'William Friedkin', 1973, 'Terror', 'Warner Bros', 'A filha de uma atriz começa a apresentar comportamentos estranhos, aparentemente possuída..'),

('Hereditary', 'Toni Collette', 'Ari Aster', 2018, 'Terror psicológico', 'A24', 'Após a morte da matriarca da família, eventos sombrios começam a afetar seus descendentes, revelando um destino amaldiçoado.'),

('The Conjuring', 'Vera Farmiga, Patrick Wilson', 'James Wan', 2013, 'Terror sobrenatural', 'New Line Cinema', 'O casal Ed e Lorraine Warren investiga a presença demoníaca que assombra uma família em sua nova casa.'),

('Midsommar', 'Florence Pugh, Jack Reynor', 'Ari Aster', 2019, 'Terror psicológico', 'A24', 'Um casal viaja para um festival sueco e descobre rituais pagãos aterrorizantes.'),

('It', 'Bill Skarsgård, Jaeden Martell', 'Andy Muschietti', 2017, 'Terror sobrenatural', 'Warner Bros', 'Um grupo de crianças enfrenta um palhaço demoníaco que se alimenta de seus medos.'),

('The Babadook', 'Essie Davis, Noah Wiseman', 'Jennifer Kent', 2014, 'Terror psicológico', 'Causeway Films', 'Uma mãe e seu filho são aterrorizados por uma entidade de um livro infantil chamado Babadook.'),

('The Witch', 'Anya Taylor-Joy, Ralph Ineson', 'Robert Eggers', 2015, 'Terror psicológico', 'A24', 'Uma família puritana acredita que uma bruxa na floresta os amaldiçoou.'),

('Halloween', 'Jamie Lee Curtis, Donald Pleasence', 'John Carpenter', 1978, 'Terror slasher', 'Compass International Pictures', 'Michael Myers escapa do sanatório e volta para matar na noite de Halloween.'),

('Scream', 'Neve Campbell, Courteney Cox, David Arquette', 'Wes Craven', 1996, 'Terror slasher', 'Dimension Films', 'Um assassino mascarado aterroriza adolescentes usando as regras dos filmes de terror.'),

('The Ring', 'Naomi Watts, Martin Henderson', 'Gore Verbinski', 2002, 'Terror sobrenatural', 'DreamWorks Pictures', 'Uma jornalista descobre uma fita amaldiçoada que mata quem a assiste após sete dias.'),

('The Blair Witch Project', 'Heather Donahue, Michael C. Williams', 'Daniel Myrick, Eduardo Sánchez', 1999, 'Terror found footage', 'Haxan Films', 'Três estudantes desaparecem enquanto filmam um documentário sobre uma bruxa.'),

('A Nightmare on Elm Street', 'Robert Englund, Heather Langenkamp, Johnny Depp', 'Wes Craven', 1984, 'Terror sobrenatural', 'New Line Cinema', 'Freddy Krueger mata adolescentes em seus pesadelos.'),

('The Texas Chainsaw Massacre', 'Marilyn Burns, Gunnar Hansen', 'Tobe Hooper', 1974, 'Terror slasher', 'Vortex Inc.', 'Um grupo de jovens é atacado por uma família de canibais liderada por Leatherface.'),

('The Nun', 'Taissa Farmiga, Demián Bichir', 'Corin Hardy', 2018, 'Terror sobrenatural', 'Warner Bros', 'Um padre e uma noviça enfrentam uma entidade demoníaca em um convento na Romênia.'),

('The Others', 'Nicole Kidman, Fionnula Flanagan', 'Alejandro Amenábar', 2001, 'Terror psicológico', 'Cruise/Wagner Productions', 'Uma mulher acredita que sua casa isolada está sendo assombrada.'),

('Insidious', 'Patrick Wilson, Rose Byrne', 'James Wan', 2010, 'Terror sobrenatural', 'Blumhouse Productions', 'Pais tentam salvar o filho preso em uma dimensão espiritual.'),

('The Silence of the Lambs', 'Jodie Foster, Anthony Hopkins', 'Jonathan Demme', 1991, 'Terror psicológico', 'Orion Pictures', 'Uma agente do FBI busca ajuda de um assassino canibal para capturar outro criminoso.'),

('Paranormal Activity', 'Katie Featherston, Micah Sloat', 'Oren Peli', 2007, 'Terror found footage', 'Blumhouse Productions', 'Um casal grava eventos sobrenaturais em sua casa.'),

('Smile', 'Sosie Bacon, Kyle Gallner', 'Parker Finn', 2022, 'Terror psicológico', 'Paramount Pictures', 'Uma psiquiatra começa a ver sorrisos perturbadores após um evento traumático.'),

('The Grudge', 'Sarah Michelle Gellar, Jason Behr', 'Takashi Shimizu', 2004, 'Terror sobrenatural', 'Ghost House Pictures', 'Uma maldição mortal condena todos que entram em contato com uma casa amaldiçoada.')
 
SELECT * FROM filme;