-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Tempo de geração: 11/05/2025 às 02:41
-- Versão do servidor: 10.4.32-MariaDB
-- Versão do PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `carros_velozes_e_furiosos`
--

-- --------------------------------------------------------

--
-- Estrutura para tabela `carro`
--

CREATE TABLE `carro` (
  `id` int(11) NOT NULL,
  `carro` varchar(100) DEFAULT NULL,
  `cor` varchar(100) DEFAULT NULL,
  `motor` varchar(100) DEFAULT NULL,
  `QuemDirigiu` varchar(100) DEFAULT NULL,
  `img` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `carro`
--

INSERT INTO `carro` (`id`, `carro`, `cor`, `motor`, `QuemDirigiu`, `img`) VALUES
(1, 'Dodge Charger R/T', 'Preto', 'V8 440 Magnum', 'Dominic Toretto', 'https://bing.com/th/id/BCO.73831fd9-0fce-4ff3-8a16-9a991643208d.png'),
(3, 'Toyota Supra', 'Laranja', '3.0 Twin-Turbo', 'Brian O’Conner', 'https://bing.com/th/id/BCO.72e57ae3-00b6-4e11-a570-f8da0e569dd7.png'),
(4, 'Nissan Skyline GT-R R34', 'Azul', 'RB26DETT 2.6L Twin-Turbo', 'Brian O’Conner', 'https://bing.com/th/id/BCO.84b68818-ba86-4d13-b14b-77aefadc0753.png'),
(5, 'Mazda RX-7 VeilSide', 'Vermelho', 'Motor Wankel 1.3L Twin-Turbo', 'Han Lue', 'https://bing.com/th/id/BCO.496a600d-c389-4c99-a798-6c99dc82e8f1.png'),
(6, 'Mitsubishi Lancer Evolution VII', 'Amarelo', '4G63 2.0 Turbo', 'Brian O’Conner', 'https://bing.com/th/id/BCO.1104a4d8-9339-46e6-a94c-1fb368ee73b3.png'),
(7, 'Honda S2000', 'Rosa', 'F22C1 2.2L', 'Suki', 'https://bing.com/th/id/BCO.905d2cd0-b695-42be-94ab-8d0e2ed16ab7.png'),
(8, 'Ford GT40', 'Azul e Branco', 'V8 5.4L', 'Equipe de Toretto', 'https://bing.com/th/id/BCO.5a7fbc42-a8fd-47c2-a145-de568a18347c.png');

--
-- Índices para tabelas despejadas
--

--
-- Índices de tabela `carro`
--
ALTER TABLE `carro`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT para tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `carro`
--
ALTER TABLE `carro`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
