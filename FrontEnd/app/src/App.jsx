import { useState,useEffect } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.scss'

function App() {
  const [carros, setCarros] = useState([]);

  useEffect(() => {
      
      fetch('http://127.0.0.1:3000/api/v1/carros/')
          .then(response => response.json())
          .then(data => setCarros(data));
  }, []);

  return (
      <div className='container'>
          <h1>Carros de Velozes e Furiosos</h1>
          <ul>
              {carros.map(carro => (
                  <li key={carro.id}>

                    <h2>{carro.carro}</h2>

                      <div className="inf">
                        <p>Cor: <span>{carro.cor}</span></p> 
                        <p>Motor: <span>{carro.motor}</span></p>
                        <p>Quem Dirigiu: <span>{carro.QuemDirigiu}</span></p>
                      </div>

                     <div className="img">
                        {carro.img ? (
                            <img src={carro.img} alt={carro.carro} srcSet="" />
                          ) : (
                            <p>Imagem não disponivel</p>
                        )}
                     </div>
                      
                    
                  </li>
         
              ))}
             
          </ul>
          
      </div>
  );
}

export default App
