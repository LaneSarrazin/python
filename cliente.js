function cliente (nome,idade){
    this.nome = nome;
    this.idade = idade;

    console.log(`meu nome e ${this.nome} e minha idade e ${this.idade}`)
}


cliente("Rosilane", 28)