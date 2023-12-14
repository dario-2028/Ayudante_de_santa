-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 14-12-2023 a las 17:39:55
-- Versión del servidor: 10.4.28-MariaDB
-- Versión de PHP: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `formularios`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `listadogarage`
--

CREATE TABLE `listadogarage` (
  `idEstacionamiento` int(11) NOT NULL,
  `nombreYapellido` varchar(100) NOT NULL,
  `marcaVehiculo` varchar(100) NOT NULL,
  `patente` int(11) NOT NULL,
  `fechaDeIngreso` date NOT NULL,
  `fechaDeEgreso` date NOT NULL,
  `foto` varchar(45) NOT NULL,
  `pago` int(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `listadogarage`
--

INSERT INTO `listadogarage` (`idEstacionamiento`, `nombreYapellido`, `marcaVehiculo`, `patente`, `fechaDeIngreso`, `fechaDeEgreso`, `foto`, `pago`) VALUES
(1, 'Nombre1 Apellido1', 'Marca1', 77777777, '2023-12-13', '2023-12-13', 'ruta_foto1.jpg', 100),
(2, 'Nombre2 Apellido2', 'Marca2', 22222222, '2023-12-13', '2023-12-13', 'ruta_foto2.jpg', 120),
(3, 'Nombre3 Apellido3', 'Marca3', 33333333, '2023-12-13', '2023-12-13', 'ruta_foto3.jpg', 90),
(4, 'Nombre4 Apellido4', 'Marca4', 0, '2023-12-13', '2023-12-13', 'ruta_foto4.jpg', 110),
(5, 'Nombre5 Apellido5', 'Marca5', 0, '2023-12-13', '2023-12-13', 'ruta_foto5.jpg', 80),
(6, 'Nombre6 Apellido6', 'Marca6', 0, '2023-12-13', '2023-12-13', 'ruta_foto6.jpg', 127),
(7, 'Nombre7 Apellido7', 'Marca7', 0, '2023-12-13', '2023-12-13', 'ruta_foto7.jpg', 127),
(8, 'Nombre8 Apellido8', 'Marca8', 0, '2023-12-13', '2023-12-13', 'ruta_foto8.jpg', 95),
(9, 'Nombre9 Apellido9', 'Marca9', 0, '2023-12-13', '2023-12-14', 'ruta_foto9.jpg', 127),
(10, 'Nombre10 Apellido10', 'Marca10', 0, '2023-12-13', '2023-12-14', 'ruta_foto10.jpg', 110),
(11, 'juan diaz', 'dogue', 0, '2023-10-11', '2023-12-14', 'foto_dogue.jpg', 0),
(12, 'julio cesar ', 'duna', 123, '2023-09-11', '2023-12-14', 'foto duna_jpg', 5000),
(13, 'julia ayende', 'mirack', 1234, '2022-11-01', '2023-12-14', 'foto.autitio.jpg', 3000),
(14, 'lili yuyo', 'camion', 33333, '2021-12-02', '2023-12-14', 'foto.camion.jpg', 39000),
(15, 'luna millei', 'duna', 99999, '2022-11-22', '2023-12-14', 'foto.camion.jpg', 39000);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `sum`
--

CREATE TABLE `sum` (
  `id` int(11) NOT NULL,
  `nombreYapellido` varchar(100) NOT NULL,
  `direccion` varchar(100) NOT NULL,
  `regalo` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `sum`
--

INSERT INTO `sum` (`id`, `nombreYapellido`, `direccion`, `regalo`) VALUES
(17, 'María Gómez', 'Avenida XYZ', 'regalo.jpg'),
(18, 'Pedro Rodriguez', 'Plaza Principal', 'regalo.jpg'),
(19, 'lolo perez', 'misiones 123', 'carbon.pg'),
(20, 'Pepe argento', 'misiones 3267', 'carbon.pg'),
(21, 'Pepa argento', 'misiones 1111', 'regalo.pg'),
(22, 'julia ayende', 'misiones 1111', 'regalo.pg'),
(23, 'juan diaz', 'misiones 123', 'regalo'),
(24, 'sofia lourdes', '5923', 'regalo'),
(25, 'luna milley', '5609', 'caja'),
(26, 'pepe argento', '780560', 'carbon'),
(28, 'lulu', 'mimi 6668', 'carbon.pg');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `listadogarage`
--
ALTER TABLE `listadogarage`
  ADD PRIMARY KEY (`idEstacionamiento`);

--
-- Indices de la tabla `sum`
--
ALTER TABLE `sum`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `listadogarage`
--
ALTER TABLE `listadogarage`
  MODIFY `idEstacionamiento` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT de la tabla `sum`
--
ALTER TABLE `sum`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=30;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
