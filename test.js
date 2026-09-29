const supernovas = [
    { nome: "Kidd", valor: 3000, status: "Ativo" },
    { nome: "Killer", valor: 200, status: "Capturado" },
    { nome: "Zoro", valor: 1111, status: "Ativo" },
    { nome: "Bege", valor: 350, status: "Ativo" },
    { nome: "Hawkins", valor: 320, status: "Capturado" },
    { nome: "Luffy", valor: 3000, status: "Ativo" }
]

const ativos = supernovas.filter(s => s.status === "Ativo")

console.log("Piratas que ainda precisam ser capturados:", ativos)

const aliancas = ativos.map(s => ({
    nome: s.nome,
    valor: s.valor * 1.2,
    status: s.status
}))

console.log("Valores alterados devido às alianças:", aliancas)

const ordemValores = aliancas.sort((a, b) => b.valor - a.valor)

console.log("Piratas por ordem do mais valioso:", ordemValores)