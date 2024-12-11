-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 11, 2024 at 02:32 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `orden_trabajo`
--

-- --------------------------------------------------------

--
-- Table structure for table `orden_trab_empleado`
--

CREATE TABLE `orden_trab_empleado` (
  `id` bigint(20) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `apellido_paterno` varchar(100) NOT NULL,
  `apellido_materno` varchar(100) NOT NULL,
  `genero` varchar(1) NOT NULL,
  `rut` varchar(12) NOT NULL,
  `fecha_nacimiento` date NOT NULL,
  `fecha_ingreso` date NOT NULL,
  `fecha_termino_contrata` date DEFAULT NULL,
  `anios_servicio` varchar(1000) NOT NULL,
  `grado` int(10) UNSIGNED NOT NULL CHECK (`grado` >= 0),
  `condicion` varchar(20) NOT NULL,
  `escalon` varchar(50) NOT NULL,
  `cargo` varchar(100) NOT NULL,
  `direccion_pertenencia` varchar(100) NOT NULL,
  `titulo_profesional` varchar(100) DEFAULT NULL,
  `situacion_actual` varchar(20) NOT NULL,
  `fecha_termino` date DEFAULT NULL,
  `observaciones` longtext NOT NULL,
  `tipo_honorario` varchar(20) DEFAULT NULL,
  `correo_electronico` varchar(255) DEFAULT NULL,
  `cta_administracion_fondos` varchar(100) DEFAULT NULL,
  `direccion` varchar(255) DEFAULT NULL,
  `etnia` varchar(100) DEFAULT NULL,
  `item_presupuestario` varchar(100) DEFAULT NULL,
  `jefatura` varchar(100) DEFAULT NULL,
  `situacion_discapacidad` varchar(100) DEFAULT NULL,
  `telefono` varchar(15) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `orden_trab_empleado`
--

INSERT INTO `orden_trab_empleado` (`id`, `nombre`, `apellido_paterno`, `apellido_materno`, `genero`, `rut`, `fecha_nacimiento`, `fecha_ingreso`, `fecha_termino_contrata`, `anios_servicio`, `grado`, `condicion`, `escalon`, `cargo`, `direccion_pertenencia`, `titulo_profesional`, `situacion_actual`, `fecha_termino`, `observaciones`, `tipo_honorario`, `correo_electronico`, `cta_administracion_fondos`, `direccion`, `etnia`, `item_presupuestario`, `jefatura`, `situacion_discapacidad`, `telefono`) VALUES
(54, 'BRENDA CAROLINA', 'ACEVEDO', 'SALAS', 'F', '9.958.110-7', '1963-11-09', '1994-06-01', '2019-12-31', '61 años 1 meses 2 días', 15, 'Planta', 'No especificado', 'Administrativo', 'SECRETARIA', 'No especificado', 'Activo(a)', NULL, 'No especificado', 'Honorario Municipal', 'brenda.acevedo@municanete.cl', 'No especificado', 'No especificada', 'No especificada', '13123123', 'No especificado', 'No', '998875020'),
(56, 'PABLO MARCOS', 'AGURTO', 'VALENCIA', 'M', '8.266.401-7', '1963-06-08', '2021-07-01', '2022-12-31', '61 años 6 meses 3 días', 11, 'Contrata', 'Técnico', 'Enc. Emergencias', 'Enc. Emergencias', 'INGENIERO EN ADM. EMPRESAS', 'Activo(a)', NULL, 'No especificado', 'No especificado', 'pablo.agurto@municanete.cl', 'No especificado', 'No especificada', 'No especificada', 'No especificado', 'No especificado', 'No', '940715643'),
(59, 'VÍCTOR RICARDO', 'BELTRÁN', 'NEIRA', 'M', '15.201.476-7', '1982-01-11', '2016-04-26', '2019-12-31', '42 años 11 meses 0 días', 19, 'Planta', 'Auxiliar', 'CONDUCTOR', 'CONDUCTOR', 'No tiene', 'Activo(a)', NULL, 'No especificado', 'No especificado', 'victor.beltran@municanete.cl', 'No especificado', 'No especificada', 'No especificada', 'No especificado', 'No especificado', 'No', '982243498'),
(60, 'CLAUDIO ENRIQUE', 'BENAVIDES', 'ÁVILA', 'M', '19.272.953-K', '1992-06-11', '2022-06-01', '2022-12-31', '32 años 6 meses 0 días', 19, 'Contrata', 'Auxiliar', 'CONDUCTOR', 'CONDUCTOR', 'No tiene', 'Activo(a)', NULL, 'No especificado', 'No especificado', 'claudio.benavides@municanete.cl', 'No especificado', 'No especificada', 'No especificada', 'No especificado', 'No especificado', 'No', '984023535'),
(61, 'HÉCTOR MAURICIO', 'BOCAZ', 'SALINAS', 'M', '13.393.484-7', '1978-05-12', '2016-01-01', '2020-12-31', '46 años 6 meses 29 días', 9, 'Planta', 'Profesional', 'Enc. Portales Web, Transparencia Municipal y arch. Digital', 'Enc. Portales Web, Transparencia Municipal y arch. Digital', 'Publicista', 'Activo(a)', NULL, 'No especificado', 'No especificado', 'mauricio.bocaz@municanete.cl', 'No especificado', 'No especificada', 'No especificada', 'No especificado', 'No especificado', 'No', '977647992');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `orden_trab_empleado`
--
ALTER TABLE `orden_trab_empleado`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `rut` (`rut`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `orden_trab_empleado`
--
ALTER TABLE `orden_trab_empleado`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=62;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
