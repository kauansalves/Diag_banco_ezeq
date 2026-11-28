CREATE TABLE login (
    id_sessao SERIAL PRIMARY KEY,
    id_cliente INT NOT NULL,
    token CHAR(64) UNIQUE NOT NULL,
 
    FOREIGN KEY (id_cliente) REFERENCES cliente(id_cliente)
);

CREATE TABLE agencia (
    id_agencia SERIAL PRIMARY KEY,
    numero CHAR(4) UNIQUE NOT NULL
);
 
CREATE TABLE tipo_operacao (
    tipo_operacao SERIAL PRIMARY KEY,
    codigo VARCHAR(12) UNIQUE NOT NULL
);

CREATE TABLE cliente (
    id_cliente SERIAL PRIMARY KEY,
    cpf CHAR(11) UNIQUE NOT NULL,
    email VARCHAR(125) UNIQUE NOT NULL
);
 
