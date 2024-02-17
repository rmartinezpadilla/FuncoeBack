-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: localhost:3306
-- Tiempo de generación: 17-02-2024 a las 15:53:47
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `funcoe_db_dev`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `advisors`
--

CREATE TABLE `advisors` (
  `uuid_advisor` varchar(255) NOT NULL,
  `document_type_uuid` varchar(255) NOT NULL,
  `identification_card` varchar(255) NOT NULL,
  `first_name` varchar(255) NOT NULL,
  `last_name` varchar(255) NOT NULL,
  `phone` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `blood_type` varchar(255) NOT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `advisors`
--

INSERT INTO `advisors` (`uuid_advisor`, `document_type_uuid`, `identification_card`, `first_name`, `last_name`, `phone`, `email`, `blood_type`, `created_at`, `updated_at`) VALUES
('42395e55-6be5-4b54-b1f7-c1536b5e3567', '71247cc6-fa87-49f3-9cb2-ff423b5a4a64', '56009000', 'carla', 'marla', '34234234', 'carla@example.com', '040420dc-ea03-4d88-bd58-b1e5f9a04785', '2024-02-17 09:26:41', '2024-02-17 09:26:41'),
('sd', '71247cc6-fa87-49f3-9cb2-ff423b5a4a64', 'ertert', 'ertert', 'ertert', 'ertert', 'ertert', '7cd905ec-e023-47bd-951c-0dea8c39758b', '2024-02-17 14:28:17', NULL),
('sdfsdf', '71247cc6-fa87-49f3-9cb2-ff423b5a4a64', 'sdf', 'sdf', 'sdf', 'sdf', 'sdf', '7cd905ec-e023-47bd-951c-0dea8c39758b', '2024-02-17 14:29:13', NULL);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `blood_type`
--

CREATE TABLE `blood_type` (
  `uuid_blood_type` varchar(255) NOT NULL,
  `blood_type` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `blood_type`
--

INSERT INTO `blood_type` (`uuid_blood_type`, `blood_type`) VALUES
('01f5a539-ad9c-4759-bbc4-bd6a816ebd85', 'A+'),
('040420dc-ea03-4d88-bd58-b1e5f9a04785', 'O+'),
('27fad2b8-5839-4c56-8c53-d7212add5867', 'A-'),
('5f6a4ccb-9b8f-4733-8ff1-cf6c36906835', 'O-'),
('658de4f8-d6ee-4bec-b4f1-94daf43f64fe', 'AB-'),
('6f454a83-4201-44e3-b7cf-99ba07464519', 'AB+'),
('7cd905ec-e023-47bd-951c-0dea8c39758b', 'B+'),
('ae8970ec-d515-427d-8a89-5b40476efe16', 'B-');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `concepts`
--

CREATE TABLE `concepts` (
  `uuid_concept` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `days`
--

CREATE TABLE `days` (
  `uuid_day` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `days`
--

INSERT INTO `days` (`uuid_day`, `name`) VALUES
('7afdd3fe-4988-43a9-92ce-1435d2123d8d', 'monday');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `documents_types`
--

CREATE TABLE `documents_types` (
  `uuid_document_type` varchar(255) NOT NULL,
  `document_type` varchar(255) NOT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `documents_types`
--

INSERT INTO `documents_types` (`uuid_document_type`, `document_type`, `created_at`, `updated_at`) VALUES
('09359aab-7354-47c0-ae6b-60d71aea3f08', 'Tarjeta de Identidad', '2024-02-02 03:41:04', NULL),
('1f88b803-880f-4b71-9a74-bc0d4ddd9bac', 'Registro Civil', '2024-02-02 03:39:41', NULL),
('71247cc6-fa87-49f3-9cb2-ff423b5a4a64', 'Cédula de ciudadanía', '2024-02-17 14:08:46', NULL),
('78ea063c-ce9c-4661-b04b-a41cf21eb83a', 'Cédula de Extranjeria', '2024-02-02 03:39:13', NULL),
('c0f535b3-1922-4322-ad23-6cb1477e56d0', 'Pasaporte', '2024-02-02 03:40:31', NULL);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `enrolls`
--

CREATE TABLE `enrolls` (
  `uuid_enroll` varchar(255) NOT NULL,
  `student_uuid` varchar(255) NOT NULL,
  `program_uuid` varchar(255) NOT NULL,
  `semester_uuid` varchar(255) NOT NULL,
  `amount` decimal(19,4) NOT NULL,
  `outstanding_balance` decimal(19,4) DEFAULT NULL,
  `positive_balance` decimal(19,2) NOT NULL,
  `dues` int(10) NOT NULL,
  `number_of_installments` int(100) NOT NULL,
  `installment_value` decimal(19,4) NOT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `enrolls`
--

INSERT INTO `enrolls` (`uuid_enroll`, `student_uuid`, `program_uuid`, `semester_uuid`, `amount`, `outstanding_balance`, `positive_balance`, `dues`, `number_of_installments`, `installment_value`, `created_at`, `updated_at`) VALUES
('26f7650d-5beb-459a-8c1a-83158a2bc080', '6595dd77-d163-47e4-8a11-03827b9bfec4', 'b082395a-50c6-48e9-a18d-0795d18c0478', 'd8392d10-6347-4b27-9fd5-1a258cae26f7', 36456.0000, 45654.0000, 45645.00, 454, 34, 234.0000, '2024-02-17 15:15:58', NULL),
('b6a3cc44-12cb-49a3-8a3d-ef577c90de62', '6595dd77-d163-47e4-8a11-03827b9bfec4', 'b082395a-50c6-48e9-a18d-0795d18c0478', 'd8392d10-6347-4b27-9fd5-1a258cae26f7', 45000.0000, 345465.0000, 45334.00, 3444, 23, 34656.0000, '2024-02-17 15:15:58', NULL);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `modules`
--

CREATE TABLE `modules` (
  `uuid_module` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `program_uuid` varchar(255) NOT NULL,
  `semester_uuid` varchar(255) NOT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `modules`
--

INSERT INTO `modules` (`uuid_module`, `name`, `program_uuid`, `semester_uuid`, `created_at`, `updated_at`) VALUES
('0fe8a909-f3b5-48d8-87a8-e547b20a1a3a', 'ingles', 'b082395a-50c6-48e9-a18d-0795d18c0478', 'd8392d10-6347-4b27-9fd5-1a258cae26f7', '2024-02-17 15:01:38', '2024-02-17 15:01:38'),
('d60fefe4-d1e1-4a8c-be8e-fd86400da6ed', 'ingles II', 'b082395a-50c6-48e9-a18d-0795d18c0478', 'd8392d10-6347-4b27-9fd5-1a258cae26f7', '2024-02-17 15:02:20', NULL);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `payments`
--

CREATE TABLE `payments` (
  `uuid_pay` varchar(255) NOT NULL,
  `enroll_uuid` varchar(255) NOT NULL,
  `concept_uuid` varchar(255) NOT NULL,
  `amount` decimal(19,4) NOT NULL,
  `pay_day` datetime NOT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `pensum`
--

CREATE TABLE `pensum` (
  `uuid_pensum` varchar(255) NOT NULL,
  `program_uuid` varchar(255) NOT NULL,
  `semester_uuid` varchar(255) NOT NULL,
  `quantity_classes` int(255) NOT NULL,
  `amount_to_paid` decimal(19,4) NOT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `pensum`
--

INSERT INTO `pensum` (`uuid_pensum`, `program_uuid`, `semester_uuid`, `quantity_classes`, `amount_to_paid`, `created_at`, `updated_at`) VALUES
('6eeb8a6a-8b47-46eb-bcd1-007f6bfe85ce', 'b082395a-50c6-48e9-a18d-0795d18c0478', 'd8392d10-6347-4b27-9fd5-1a258cae26f7', 34, 23545.0000, '2024-02-17 15:20:28', NULL),
('7e51a542-9622-420e-a884-087d9aa6e4ac', 'b082395a-50c6-48e9-a18d-0795d18c0478', 'd8392d10-6347-4b27-9fd5-1a258cae26f7', 34, 343545.0000, '2024-02-17 15:20:28', NULL);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `programs`
--

CREATE TABLE `programs` (
  `uuid_program` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `programs`
--

INSERT INTO `programs` (`uuid_program`, `name`, `created_at`, `updated_at`) VALUES
('b082395a-50c6-48e9-a18d-0795d18c0478', 'Sistemas Básico', '2024-02-17 14:45:09', NULL);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `roles`
--

CREATE TABLE `roles` (
  `uuid_rol` varchar(255) NOT NULL,
  `name_rol` varchar(255) NOT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `roles`
--

INSERT INTO `roles` (`uuid_rol`, `name_rol`, `created_at`, `updated_at`) VALUES
('da6669bd-e15a-4d06-bc01-a4d0d227e738', 'admin', '2024-02-17 01:49:03', NULL);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `semesters`
--

CREATE TABLE `semesters` (
  `uuid_semester` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `semesters`
--

INSERT INTO `semesters` (`uuid_semester`, `name`, `created_at`, `updated_at`) VALUES
('d8392d10-6347-4b27-9fd5-1a258cae26f7', '1', '2024-02-17 14:43:22', NULL);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `shifts`
--

CREATE TABLE `shifts` (
  `uuid_shifts` varchar(255) NOT NULL,
  `module_uuid` varchar(255) NOT NULL,
  `amount_hours` int(10) NOT NULL,
  `salary` decimal(19,4) NOT NULL,
  `created_at` datetime NOT NULL,
  `teacher_uuid` varchar(255) NOT NULL,
  `updated_at` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `shifts`
--

INSERT INTO `shifts` (`uuid_shifts`, `module_uuid`, `amount_hours`, `salary`, `created_at`, `teacher_uuid`, `updated_at`) VALUES
('cee0c0d4-4bfb-461e-8633-e6ea54a2ed6e', '0fe8a909-f3b5-48d8-87a8-e547b20a1a3a', 34, 345345.0000, '2024-02-17 15:04:15', '1ff7d878-c25d-4c0a-a0ec-b21cdebb5e8c', NULL),
('ddaeade6-c8ef-4e8c-ac57-b25af8578442', '0fe8a909-f3b5-48d8-87a8-e547b20a1a3a', 32, 45345.0000, '2024-02-17 15:04:15', '1ff7d878-c25d-4c0a-a0ec-b21cdebb5e8c', NULL);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `students`
--

CREATE TABLE `students` (
  `uuid_student` varchar(255) NOT NULL,
  `document_type_uuid` varchar(255) NOT NULL,
  `identification_card` varchar(255) NOT NULL,
  `birthdate` date NOT NULL DEFAULT current_timestamp(),
  `first_name` varchar(255) NOT NULL,
  `last_name` varchar(255) NOT NULL,
  `municipality` varchar(255) NOT NULL,
  `address` varchar(255) NOT NULL,
  `phone` varchar(20) NOT NULL,
  `gender` varchar(255) DEFAULT NULL,
  `blood_type` varchar(255) NOT NULL,
  `recommendation` varchar(255) NOT NULL,
  `advertising_medium` varchar(255) NOT NULL,
  `day_uuid` varchar(255) NOT NULL,
  `created_at` datetime NOT NULL,
  `working_day` varchar(255) NOT NULL,
  `registration_number` int(11) NOT NULL,
  `advisor_uuid` varchar(255) NOT NULL,
  `updated_at` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `students`
--

INSERT INTO `students` (`uuid_student`, `document_type_uuid`, `identification_card`, `birthdate`, `first_name`, `last_name`, `municipality`, `address`, `phone`, `gender`, `blood_type`, `recommendation`, `advertising_medium`, `day_uuid`, `created_at`, `working_day`, `registration_number`, `advisor_uuid`, `updated_at`) VALUES
('6595dd77-d163-47e4-8a11-03827b9bfec4', '71247cc6-fa87-49f3-9cb2-ff423b5a4a64', '20000', '1989-02-01', 'lore', 'caba', 'mont', 'cl23 dfdf', '234234', 'fem', '7cd905ec-e023-47bd-951c-0dea8c39758b', 'n/a', 'n/a', '7afdd3fe-4988-43a9-92ce-1435d2123d8d', '2024-02-17 14:38:54', 'mon', 234234, 'sd', '2024-02-17 14:38:54'),
('d300cfc5-0768-4e21-985e-51ef4bcf82a1', '71247cc6-fa87-49f3-9cb2-ff423b5a4a64', '90000', '1990-02-01', 'home', 'macri', 'CRT', 'cll 45-sd', '43345565', 'fem', '7cd905ec-e023-47bd-951c-0dea8c39758b', 'assdasd', 'asdasd', '7afdd3fe-4988-43a9-92ce-1435d2123d8d', '2024-02-17 14:38:54', 'mon', 234234, 'sd', '2024-02-17 14:38:54');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `teachers`
--

CREATE TABLE `teachers` (
  `uuid_teacher` varchar(255) NOT NULL,
  `document_type_uuid` varchar(255) NOT NULL,
  `identification_card` varchar(255) NOT NULL,
  `first_name` varchar(255) NOT NULL,
  `last_name` varchar(255) NOT NULL,
  `blood_type_uuid` varchar(255) NOT NULL,
  `phone` varchar(255) NOT NULL,
  `user` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `created_at` datetime NOT NULL,
  `last_connection` datetime DEFAULT NULL,
  `program_uuid` varchar(255) NOT NULL,
  `updated_at` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `teachers`
--

INSERT INTO `teachers` (`uuid_teacher`, `document_type_uuid`, `identification_card`, `first_name`, `last_name`, `blood_type_uuid`, `phone`, `user`, `password`, `created_at`, `last_connection`, `program_uuid`, `updated_at`) VALUES
('1ff7d878-c25d-4c0a-a0ec-b21cdebb5e8c', '71247cc6-fa87-49f3-9cb2-ff423b5a4a64', '56000000', 'ere', 'sdf', '7cd905ec-e023-47bd-951c-0dea8c39758b', '45345', 'rte', 'ert', '2024-02-17 14:50:14', NULL, 'b082395a-50c6-48e9-a18d-0795d18c0478', NULL),
('be951fb6-785b-496c-939a-e96d8b45560a', '71247cc6-fa87-49f3-9cb2-ff423b5a4a64', '521111111', 'doc', 'doc 1', '7cd905ec-e023-47bd-951c-0dea8c39758b', '3433333', 'user', 'user', '2024-02-17 08:49:19', NULL, 'b082395a-50c6-48e9-a18d-0795d18c0478', '2024-02-17 14:48:07'),
('cb36dc02-b50c-4b35-9c5d-cb1939fea51e', '71247cc6-fa87-49f3-9cb2-ff423b5a4a64', '8900000', 'doc doc', 'doc doc II', '7cd905ec-e023-47bd-951c-0dea8c39758b', '5454545', 'docuser', 'docuser', '2024-02-17 08:49:19', NULL, 'b082395a-50c6-48e9-a18d-0795d18c0478', '2024-02-17 14:48:07');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `users`
--

CREATE TABLE `users` (
  `uuid_user` varchar(255) NOT NULL,
  `document_type_uuid` varchar(255) NOT NULL,
  `identification_card` varchar(255) NOT NULL,
  `first_name` varchar(255) NOT NULL,
  `rol_uuid` varchar(255) NOT NULL,
  `user` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime DEFAULT NULL,
  `last_connection` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `users`
--

INSERT INTO `users` (`uuid_user`, `document_type_uuid`, `identification_card`, `first_name`, `rol_uuid`, `user`, `password`, `is_active`, `created_at`, `updated_at`, `last_connection`) VALUES
('48ae7b06-bdc8-492f-b030-19937b16953d', '71247cc6-fa87-49f3-9cb2-ff423b5a4a64', '23232', 'sdfdf', 'da6669bd-e15a-4d06-bc01-a4d0d227e738', 'yo', 'tu', 1, '2024-02-17 15:13:49', NULL, NULL),
('f3be89ae-b09c-4fb2-8ed0-214789bc4175', '71247cc6-fa87-49f3-9cb2-ff423b5a4a64', '7567567', 'tyghj', 'da6669bd-e15a-4d06-bc01-a4d0d227e738', 'mnm', 'nmn', 0, '2024-02-17 15:13:49', NULL, NULL);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `advisors`
--
ALTER TABLE `advisors`
  ADD PRIMARY KEY (`uuid_advisor`),
  ADD UNIQUE KEY `identification_card` (`identification_card`),
  ADD KEY `document_type_uuid_fk_01` (`document_type_uuid`),
  ADD KEY `blood_type` (`blood_type`);

--
-- Indices de la tabla `blood_type`
--
ALTER TABLE `blood_type`
  ADD PRIMARY KEY (`uuid_blood_type`);

--
-- Indices de la tabla `concepts`
--
ALTER TABLE `concepts`
  ADD PRIMARY KEY (`uuid_concept`);

--
-- Indices de la tabla `days`
--
ALTER TABLE `days`
  ADD PRIMARY KEY (`uuid_day`);

--
-- Indices de la tabla `documents_types`
--
ALTER TABLE `documents_types`
  ADD PRIMARY KEY (`uuid_document_type`);

--
-- Indices de la tabla `enrolls`
--
ALTER TABLE `enrolls`
  ADD PRIMARY KEY (`uuid_enroll`),
  ADD KEY `estudiante_id` (`student_uuid`),
  ADD KEY `programa_id` (`program_uuid`),
  ADD KEY `semestre` (`semester_uuid`);

--
-- Indices de la tabla `modules`
--
ALTER TABLE `modules`
  ADD PRIMARY KEY (`uuid_module`),
  ADD KEY `programa_id` (`program_uuid`),
  ADD KEY `semestre_2` (`semester_uuid`);

--
-- Indices de la tabla `payments`
--
ALTER TABLE `payments`
  ADD PRIMARY KEY (`uuid_pay`),
  ADD KEY `estudiante_id` (`enroll_uuid`),
  ADD KEY `concepto_id` (`concept_uuid`),
  ADD KEY `matricula_id` (`enroll_uuid`);

--
-- Indices de la tabla `pensum`
--
ALTER TABLE `pensum`
  ADD PRIMARY KEY (`uuid_pensum`),
  ADD KEY `programa_id` (`program_uuid`),
  ADD KEY `semestre_id` (`semester_uuid`),
  ADD KEY `program_uuid` (`program_uuid`),
  ADD KEY `semester_uuid` (`semester_uuid`);

--
-- Indices de la tabla `programs`
--
ALTER TABLE `programs`
  ADD PRIMARY KEY (`uuid_program`);

--
-- Indices de la tabla `roles`
--
ALTER TABLE `roles`
  ADD PRIMARY KEY (`uuid_rol`);

--
-- Indices de la tabla `semesters`
--
ALTER TABLE `semesters`
  ADD PRIMARY KEY (`uuid_semester`);

--
-- Indices de la tabla `shifts`
--
ALTER TABLE `shifts`
  ADD PRIMARY KEY (`uuid_shifts`),
  ADD KEY `modulo_id` (`module_uuid`),
  ADD KEY `docente_id` (`teacher_uuid`);

--
-- Indices de la tabla `students`
--
ALTER TABLE `students`
  ADD PRIMARY KEY (`uuid_student`),
  ADD KEY `asesor_id` (`advisor_uuid`),
  ADD KEY `dia_id` (`day_uuid`),
  ADD KEY `document_type_ibfk_2` (`document_type_uuid`),
  ADD KEY `document_type_uuid` (`document_type_uuid`),
  ADD KEY `blood_type` (`blood_type`);

--
-- Indices de la tabla `teachers`
--
ALTER TABLE `teachers`
  ADD PRIMARY KEY (`uuid_teacher`),
  ADD KEY `programa_id` (`program_uuid`),
  ADD KEY `my_blood_type` (`blood_type_uuid`),
  ADD KEY `my_document_type` (`document_type_uuid`),
  ADD KEY `document_type_uuid` (`document_type_uuid`);

--
-- Indices de la tabla `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`uuid_user`),
  ADD KEY `fk_document_type` (`document_type_uuid`),
  ADD KEY `fk_rol_uuid` (`rol_uuid`);

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `advisors`
--
ALTER TABLE `advisors`
  ADD CONSTRAINT `blood_type_uuid_fk3` FOREIGN KEY (`blood_type`) REFERENCES `blood_type` (`uuid_blood_type`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `document_type_fk45` FOREIGN KEY (`document_type_uuid`) REFERENCES `documents_types` (`uuid_document_type`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `enrolls`
--
ALTER TABLE `enrolls`
  ADD CONSTRAINT `program_fk_02` FOREIGN KEY (`program_uuid`) REFERENCES `programs` (`uuid_program`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `semester_fk_03` FOREIGN KEY (`semester_uuid`) REFERENCES `semesters` (`uuid_semester`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `student_fk_01` FOREIGN KEY (`student_uuid`) REFERENCES `students` (`uuid_student`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `modules`
--
ALTER TABLE `modules`
  ADD CONSTRAINT `fk_programs_f1` FOREIGN KEY (`program_uuid`) REFERENCES `programs` (`uuid_program`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_smesters_f2` FOREIGN KEY (`semester_uuid`) REFERENCES `semesters` (`uuid_semester`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `pensum`
--
ALTER TABLE `pensum`
  ADD CONSTRAINT `program_fk_2` FOREIGN KEY (`program_uuid`) REFERENCES `programs` (`uuid_program`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `semesters_fk_2` FOREIGN KEY (`semester_uuid`) REFERENCES `semesters` (`uuid_semester`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `shifts`
--
ALTER TABLE `shifts`
  ADD CONSTRAINT `module_fk_01` FOREIGN KEY (`module_uuid`) REFERENCES `modules` (`uuid_module`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `teacher_fk_02` FOREIGN KEY (`teacher_uuid`) REFERENCES `teachers` (`uuid_teacher`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `students`
--
ALTER TABLE `students`
  ADD CONSTRAINT `advisor_fk_01` FOREIGN KEY (`advisor_uuid`) REFERENCES `advisors` (`uuid_advisor`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `blood_type_fk_2` FOREIGN KEY (`blood_type`) REFERENCES `blood_type` (`uuid_blood_type`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `day_fk_2` FOREIGN KEY (`day_uuid`) REFERENCES `days` (`uuid_day`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `document_type_ibfk_2` FOREIGN KEY (`document_type_uuid`) REFERENCES `documents_types` (`uuid_document_type`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `teachers`
--
ALTER TABLE `teachers`
  ADD CONSTRAINT `blood_type_f01` FOREIGN KEY (`blood_type_uuid`) REFERENCES `blood_type` (`uuid_blood_type`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `document_type_kf30` FOREIGN KEY (`document_type_uuid`) REFERENCES `documents_types` (`uuid_document_type`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `program_uuid_fk` FOREIGN KEY (`program_uuid`) REFERENCES `programs` (`uuid_program`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `users`
--
ALTER TABLE `users`
  ADD CONSTRAINT `document_type_fk90` FOREIGN KEY (`document_type_uuid`) REFERENCES `documents_types` (`uuid_document_type`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_rol_uuid` FOREIGN KEY (`rol_uuid`) REFERENCES `roles` (`uuid_rol`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
