.open agenda.db
.mode table

drop table if exists contato;

CREATE TABLE contato (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT UNIQUE NOT NULL,
    data_nascimento DATE NOT NULL
);

drop table if exists edereco;

CREATE TABLE endereco (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    rua TEXT NOT NULL,
    numero TEXT NOT NULL,
    complemento TEXT,
    bairro TEXT NOT NULL,
    municipio TEXT NOT NULL,
    estado TEXT NOT NULL,
    cep TEXT NOT NULL,
    contato_id INTEGER UNIQUE NOT NULL,
    FOREIGN KEY (contato_id) REFERENCES contato(id) ON DELETE CASCADE
);

drop table if exists telefone;

CREATE TABLE telefone (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    numero TEXT NOT NULL,
    contato_id INTEGER NOT NULL,
    FOREIGN KEY (contato_id) REFERENCES contato(id) ON DELETE CASCADE
);

drop table if exists email;


CREATE TABLE email (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT NOT NULL,
    contato_id INTEGER NOT NULL,
    FOREIGN KEY (contato_id) REFERENCES contato(id) ON DELETE CASCADE
);
