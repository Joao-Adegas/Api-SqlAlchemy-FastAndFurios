import { useState,useEffect } from 'react'
import reactLogo from './assets/react.svg'
import './App.scss'
import {Swiper,SwiperSlide} from 'swiper/react'
import {Navigation} from 'swiper/modules'
import 'swiper/css'
import 'swiper/css/navigation'



function App() {
  const [carros, setCarros] = useState([]);
  const [currentIndex, setcurrentIndex] = useState([]);

  const backgroundColors = {
    "Mazda RX-7 VeilSide": "#8B0000",
    "Nissan Skyline GT-R R34": "#003366",
    "Mitsubishi Lancer Evolution VII": "#FFD700",
    "Toyota Supra": "#FFA500",
    "Honda S2000": "#FF69B4",
    "Ford GT40": "#1E90FF",
    "Lykan Hypersport": "#DC143C"
  };

  useEffect(() => {
      
      fetch('http://127.0.0.1:3000/api/v1/carros/')
          .then(response => response.json())
          .then(data => setCarros(data));
  }, []);

  return (
    
    <div className='container'>
      <Swiper
        modules={[Navigation]}
        slidesPerView={1}
        pagination={{ clickable: true }} 
        navigation={true}
        autoplay={true}
      >
        {carros.map((carro) => (
          <SwiperSlide key={carro.id}>
            <div className="inf">
              <h1>{carro.id}</h1>

              <div className="slide-item">
                <img src={carro.img} alt={carro.carro} />
                <div className="border-animation"></div>
              </div>

              <div className="inf infLeft">
                <div className="Personagem">
                  <span>{carro.QuemDirigiu}</span>
                </div>

                <div className="nome">
                  <span>{carro.carro}</span>
                </div>

                <div className="motor">
                  <span>{carro.motor}</span>
                </div>

              </div>
            </div>
          </SwiperSlide>
        ))}
      </Swiper>  
          
      </div>
  );
}

export default App
