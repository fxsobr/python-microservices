import React, {useEffect, useState} from 'react';
import {ProdutoMain} from "../interfaces/produto";

const Main = () => {
    const [produtos, setProdutos] = useState([] as ProdutoMain[])

    useEffect(() => {
        (
            async () => {
                const response = await fetch('http://localhost:8001/api/produtos')
                const data = await response.json()

                setProdutos(data)
            }
        )()
    }, [])

    const curtidas = async (id: number) => {
        await fetch(`http://localhost:8001/api/produtos/${id}/curtida`, {
            method: 'POST',
            headers: {'Content-Type': 'application/json'}
        })

        setProdutos(produtos.map(
            (p: ProdutoMain) => {
                if (p.id === id) {
                    p.curtidas++;
                }

                return p;
            }
        ))
    }

    return (
        <div>
            <main>
                <div className="album py-5 bg-light">
                    <div className="container">
                        <div className="row row-cols-1 row-cols-sm-2 row-cols-md-3 g-3">
                            {produtos.map(
                                (p: ProdutoMain) => {
                                    return (
                                        <div className="col" key={p.id}>
                                            <div className="card shadow-sm">
                                                <img src={p.image} height={180} />
                                                <div className="card-body">
                                                    <p className="card-text">{p.titulo}</p>
                                                    <div className="d-flex justify-content-between align-items-center">
                                                        <div className="btn-group">
                                                            <button type="button"
                                                                    className="btn btn-sm btn-outline-secondary"
                                                                    onClick={() => curtidas(p.id)}
                                                                    >Curtir
                                                            </button>
                                                        </div>
                                                        <small className="text-muted">{p.curtidas} Curtidas</small>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                    )
                                }
                            )}
                        </div>
                    </div>
                </div>

            </main>
        </div>
    );
};

export default Main;