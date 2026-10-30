create database proyecto_final_mpd

--- Creacion de tabla carrera ---
create table carrera ( 
carrera_id char (50)  primary key not null,
facultad_id varchar (50) not null,
duracion_semestre int not null,
titulo_otorgado char (50) not null);




--- Creacion de tabla matricula ---
create table matricula (
matricula_id char (10)  primary key not null,
estudiante_id varchar (50) not null,
curso_id varchar (50) not null,
fecha_registro date not null);

--- Creacion de tabla curso ---
create table curso (
curso_id varchar (10)  primary key not null,
nombre_curso varchar (50) not null,
credito_del_curso int not null);

--- Creacion de tabla profesor ---
create table profesor (
profesor_id int primary key not null,
nombre varchar (50) not null,
apellido varchar (50) not null,
email varchar (50) not null,
nombre_curso varchar (50) not null,
es_tiempo_completo BIT NOT NULL DEFAULT 1); -- Permite identificar si un docente es de tiempo completo (1) o por horas (0)

--- Creacion de tabla pago ---
create table pago (
    pago_id int identity(1,1) primary key, 
    matricula_id varchar(30) not null,
    monto decimal (10,2) not null,
    fecha_pago date not null,
    metodo_pago varchar(30) null);

    
---Creacion tabla detalle-matricula---

create table dbo.detalle_matricula (
    detalle_id int identity(11999,1) primary key not null,
    matricula_id char(10) not null,
    periodo_id int not null,
    estado_curso varchar(35) null check (estado_curso in ('activo', 'inactivo')),
    nombre_periodo varchar(20) not null,
    fecha_inicio date not null,
    fecha_fin date not null
);

--- creacion de tabla estudiante ---
create table estudiante (
    estudiante_id varchar(50) primary key not null,
    nombre varchar(50) not null,
    apellido varchar(50) not null,
    telefono int null,
    email varchar(50) not null,
    estado_de_actividad varchar(10) not null check (estado_de_actividad in ('activo', 'inactivo')),
    carrera_id char(50) not null,
    curso_id varchar(10) not null,
    profesor_id int null,
    periodo_id int not null,
    aula varchar(20) null,
    dia_semana varchar(15) not null,   -- ej: 'lunes', 'miercoles'
    hora_inicio time not null,  
    hora_fin time not null      
);    



--- Creacion de tabla facultad ---
    create table facultad (
    facultad_id varchar(20) primary key not null,
    nombre_facultad varchar (100) not null,
    edificio varchar(50) not null,
    decano varchar (100) null --- se coloco null porque este campo puede quedarse vacío o no tener un valor asignado por ahora, porque puede que no haya decano
);

--- Creacion de tabla factura ---
    create table dbo.factura (
    factura_id int IDENTITY(30000, 1) primary key not null,
    estudiante_id varchar(50) not null,
    fecha_emision date not null,
    monto_total int not null 
);

---Bases de datos----
---Insertar Base de datos carrera---
INSERT INTO dbo.carrera (carrera_id, facultad_id, duracion_semestre, titulo_otorgado) VALUES
('CAR-001', 'FAC-ING', 10, 'Ingeniero en Sistemas'),
('CAR-002', 'FAC-CED', 8, 'Licenciado en Administración'),
('CAR-003', 'FAC-SAL', 10, 'Doctor en Medicina'),
('CAR-004', 'FAC-DER', 10, 'Licenciado en Derecho'),
('CAR-005', 'FAC-EDU', 8, 'Licenciado en Educación'),
('CAR-006', 'FAC-ING', 10, 'Ingeniero Industrial'),
('CAR-007', 'FAC-CED', 8, 'Contador Público'),
('CAR-008', 'FAC-SAL', 8, 'Licenciado en Enfermería'),
('CAR-009', 'FAC-ING', 8, 'Diseñador Gráfico'),
('CAR-010', 'FAC-CED', 8, 'Licenciado en Mercadeo'),
('CAR-011', 'FAC-ING', 10, 'Ingeniero en Sistemas'),
('CAR-012', 'FAC-CED', 8, 'Licenciado en Administración'),
('CAR-013', 'FAC-SAL', 10, 'Doctor en Medicina'),
('CAR-014', 'FAC-DER', 10, 'Licenciado en Derecho'),
('CAR-015', 'FAC-EDU', 8, 'Licenciado en Educación'),
('CAR-016', 'FAC-ING', 10, 'Ingeniero Industrial'),
('CAR-017', 'FAC-CED', 8, 'Contador Público'),
('CAR-018', 'FAC-SAL', 8, 'Licenciado en Enfermería'),
('CAR-019', 'FAC-ING', 8, 'Diseñador Gráfico'),
('CAR-020', 'FAC-CED', 8, 'Licenciado en Mercadeo'),
('CAR-021', 'FAC-ING', 10, 'Ingeniero en Sistemas'),
('CAR-022', 'FAC-CED', 8, 'Licenciado en Administración'),
('CAR-023', 'FAC-SAL', 10, 'Doctor en Medicina'),
('CAR-024', 'FAC-DER', 10, 'Licenciado en Derecho'),
('CAR-025', 'FAC-EDU', 8, 'Licenciado en Educación'),
('CAR-026', 'FAC-ING', 10, 'Ingeniero Industrial'),
('CAR-027', 'FAC-CED', 8, 'Contador Público'),
('CAR-028', 'FAC-SAL', 8, 'Licenciado en Enfermería'),
('CAR-029', 'FAC-ING', 8, 'Diseñador Gráfico'),
('CAR-030', 'FAC-CED', 8, 'Licenciado en Mercadeo'),
('CAR-031', 'FAC-ING', 10, 'Ingeniero en Sistemas'),
('CAR-032', 'FAC-CED', 8, 'Licenciado en Administración'),
('CAR-033', 'FAC-SAL', 10, 'Doctor en Medicina'),
('CAR-034', 'FAC-DER', 10, 'Licenciado en Derecho'),
('CAR-035', 'FAC-EDU', 8, 'Licenciado en Educación'),
('CAR-036', 'FAC-ING', 10, 'Ingeniero Industrial'),
('CAR-037', 'FAC-CED', 8, 'Contador Público'),
('CAR-038', 'FAC-SAL', 8, 'Licenciado en Enfermería'),
('CAR-039', 'FAC-ING', 8, 'Diseñador Gráfico'),
('CAR-040', 'FAC-CED', 8, 'Licenciado en Mercadeo'),
('CAR-041', 'FAC-ING', 10, 'Ingeniero en Sistemas'),
('CAR-042', 'FAC-CED', 8, 'Licenciado en Administración'),
('CAR-043', 'FAC-SAL', 10, 'Doctor en Medicina'),
('CAR-044', 'FAC-DER', 10, 'Licenciado en Derecho'),
('CAR-045', 'FAC-EDU', 8, 'Licenciado en Educación'),
('CAR-046', 'FAC-ING', 10, 'Ingeniero Industrial'),
('CAR-047', 'FAC-CED', 8, 'Contador Público'),
('CAR-048', 'FAC-SAL', 8, 'Licenciado en Enfermería'),
('CAR-049', 'FAC-ING', 8, 'Diseñador Gráfico'),
('CAR-050', 'FAC-CED', 8, 'Licenciado en Mercadeo');

--- insertar datos en la tabla estudiante ---
insert into dbo.estudiante (
    estudiante_id, nombre, apellido, telefono, email, estado_de_actividad, carrera_id, curso_id, profesor_id, periodo_id, aula, dia_semana, hora_inicio, hora_fin
) values
('EST-001', 'Carlos', 'Gómez', 88881001, 'cgomez001@estudiante.edu', 'Activo', 'CAR-001', 'CUR-BD1', 101, 202601, 'Lab 3', 'Lunes', '08:00:00', '11:00:00'),
('EST-002', 'María', 'Rodríguez', 88881002, 'mrodriguez002@estudiante.edu', 'Activo', 'CAR-002', 'CUR-CNT', 102, 202601, 'Aula 201', 'Miércoles', '13:00:00', '16:00:00'),
('EST-003', 'Juan', 'Fernández', 88881003, 'jfernandez003@estudiante.edu', 'Inactivo', 'CAR-003', 'CUR-PRO', 101, 202601, 'Lab 1', 'Martes', '08:00:00', '11:00:00'),
('EST-004', 'Ana', 'López', 88881004, 'alopez004@estudiante.edu', 'Activo', 'CAR-004', 'CUR-CNT', 102, 202601, 'Aula 201', 'Miércoles', '13:00:00', '16:00:00'),
('EST-005', 'Luis', 'Martínez', 88881005, 'lmartinez005@estudiante.edu', 'Activo', 'CAR-005', 'CUR-BD1', 101, 202601, 'Lab 3', 'Lunes', '08:00:00', '11:00:00'),
('EST-006', 'Laura', 'Sánchez', 88881006, 'lsanchez006@estudiante.edu', 'Inactivo', 'CAR-006', 'CUR-MAT', 102, 202601, 'Aula 105', 'Jueves', '10:00:00', '13:00:00'),
('EST-007', 'Pedro', 'Pérez', 88881007, 'pperez007@estudiante.edu', 'Activo', 'CAR-007', 'CUR-BD1', 101, 202601, 'Lab 3', 'Lunes', '08:00:00', '11:00:00'),
('EST-008', 'Sofia', 'González', 88881008, 'sgonzalez008@estudiante.edu', 'Activo', 'CAR-008', 'CUR-CNT', 102, 202601, 'Aula 201', 'Miércoles', '13:00:00', '16:00:00'),
('EST-009', 'Diego', 'Ramírez', 88881009, 'dramirez009@estudiante.edu', 'Activo', 'CAR-009', 'CUR-DER', 101, 202601, 'Aula 302', 'Viernes', '14:00:00', '17:00:00'),
('EST-010', 'Elena', 'Torres', 88881010, 'etorres010@estudiante.edu', 'Inactivo', 'CAR-010', 'CUR-CNT', 102, 202601, 'Aula 201', 'Miércoles', '13:00:00', '16:00:00'),
('EST-011', 'Gabriel', 'Vargas', 88881011, 'gvargas011@estudiante.edu', 'Activo', 'CAR-011', 'CUR-BD1', 101, 202601, 'Lab 3', 'Lunes', '08:00:00', '11:00:00'),
('EST-012', 'Lucía', 'Castro', 88881012, 'lcastro012@estudiante.edu', 'Activo', 'CAR-012', 'CUR-ADM', 102, 202601, 'Aula 204', 'Lunes', '18:00:00', '21:00:00'),
('EST-013', 'Mateo', 'Morales', 88881013, 'mmorales013@estudiante.edu', 'Activo', 'CAR-013', 'CUR-BD1', 101, 202601, 'Lab 3', 'Lunes', '08:00:00', '11:00:00'),
('EST-014', 'Paula', 'Herrera', 88881014, 'pherrera014@estudiante.edu', 'Inactivo', 'CAR-014', 'CUR-CNT', 102, 202601, 'Aula 201', 'Miércoles', '13:00:00', '16:00:00'),
('EST-015', 'Andrés', 'Jiménez', 88881015, 'ajimenez015@estudiante.edu', 'Activo', 'CAR-015', 'CUR-BD1', 101, 202601, 'Lab 3', 'Lunes', '08:00:00', '11:00:00'),
('EST-016', 'Camila', 'Rojas', 88881016, 'crojas016@estudiante.edu', 'Activo', 'CAR-016', 'CUR-MED', 101, 202601, 'Lab Biología', 'Sábado', '08:00:00', '12:00:00'),
('EST-017', 'Javier', 'Díaz', 88881017, 'jdiaz017@estudiante.edu', 'Activo', 'CAR-017', 'CUR-BD1', 101, 202601, 'Lab 3', 'Lunes', '08:00:00', '11:00:00'),
('EST-018', 'Valeria', 'Alvarado', 88881018, 'valvarado018@estudiante.edu', 'Inactivo', 'CAR-018', 'CUR-CNT', 102, 202601, 'Aula 201', 'Miércoles', '13:00:00', '16:00:00'),
('EST-019', 'Daniel', 'Soto', 88881019, 'dsoto019@estudiante.edu', 'Activo', 'CAR-019', 'CUR-EDU', 102, 202601, 'Aula 108', 'Martes', '13:00:00', '16:00:00'),
('EST-020', 'Mariana', 'Navarro', 88881020, 'mnavarro020@estudiante.edu', 'Activo', 'CAR-020', 'CUR-CNT', 102, 202601, 'Aula 201', 'Miércoles', '13:00:00', '16:00:00'),
('EST-021', 'Alejandro', 'Mendoza', 88881021, 'amendoza021@estudiante.edu', 'Activo', 'CAR-021', 'CUR-BD1', 101, 202601, 'Lab 3', 'Lunes', '08:00:00', '11:00:00'),
('EST-022', 'Natalia', 'Araya', 88881022, 'naraya022@estudiante.edu', 'Inactivo', 'CAR-022', 'CUR-EST', 101, 202601, 'Aula 102', 'Miércoles', '08:00:00', '11:00:00'),
('EST-023', 'Fernando', 'Solano', 88881023, 'fsolano023@estudiante.edu', 'Activo', 'CAR-023', 'CUR-BD1', 101, 202601, 'Lab 3', 'Lunes', '08:00:00', '11:00:00'),
('EST-024', 'Daniela', 'Aguilar', 88881024, 'daguilar024@estudiante.edu', 'Activo', 'CAR-024', 'CUR-CNT', 102, 202601, 'Aula 201', 'Miércoles', '13:00:00', '16:00:00'),
('EST-025', 'Ricardo', 'Campos', 88881025, 'rcampos025@estudiante.edu', 'Activo', 'CAR-025', 'CUR-MKT', 102, 202601, 'Aula 205', 'Jueves', '18:00:00', '21:00:00'),
('EST-026', 'Victoria', 'Vega', 88881026, 'vvega026@estudiante.edu', 'Inactivo', 'CAR-026', 'CUR-CNT', 102, 202601, 'Aula 201', 'Miércoles', '13:00:00', '16:00:00'),
('EST-027', 'Manuel', 'Chaves', 88881027, 'mchaves027@estudiante.edu', 'Activo', 'CAR-027', 'CUR-BD1', 101, 202601, 'Lab 3', 'Lunes', '08:00:00', '11:00:00'),
('EST-028', 'Isabel', 'Mora', 88881028, 'imora028@estudiante.edu', 'Activo', 'CAR-028', 'CUR-ALG', 101, 202601, 'Aula 101', 'Lunes', '08:00:00', '11:00:00'),
('EST-029', 'Hugo', 'Blanco', 88881029, 'hblanco029@estudiante.edu', 'Activo', 'CAR-029', 'CUR-BD1', 101, 202601, 'Lab 3', 'Lunes', '08:00:00', '11:00:00'),
('EST-030', 'Beatriz', 'Cordero', 88881030, 'bcordero030@estudiante.edu', 'Inactivo', 'CAR-030', 'CUR-CNT', 102, 202601, 'Aula 201', 'Miércoles', '13:00:00', '16:00:00'),
('EST-031', 'Adrian', 'Reyes', 88881031, 'areyes031@estudiante.edu', 'Activo', 'CAR-031', 'CUR-CAL2', 102, 202601, 'Aula 103', 'Martes', '11:00:00', '14:00:00'),
('EST-032', 'Silvia', 'Méndez', 88881032, 'smendez032@estudiante.edu', 'Activo', 'CAR-032', 'CUR-CNT', 102, 202601, 'Aula 201', 'Miércoles', '13:00:00', '16:00:00'),
('EST-033', 'Jorge', 'Gutiérrez', 88881033, 'jgutierrez033@estudiante.edu', 'Activo', 'CAR-033', 'CUR-BD1', 101, 202601, 'Lab 3', 'Lunes', '08:00:00', '11:00:00'),
('EST-034', 'Patricia', 'Salazar', 88881034, 'psalazar034@estudiante.edu', 'Inactivo', 'CAR-034', 'CUR-EDO', 101, 202601, 'Aula 104', 'Miércoles', '14:00:00', '17:00:00'),
('EST-035', 'Roberto', 'Arias', 88881035, 'rarias035@estudiante.edu', 'Activo', 'CAR-035', 'CUR-BD1', 101, 202601, 'Lab 3', 'Lunes', '08:00:00', '11:00:00'),
('EST-036', 'Claudia', 'Guzmán', 88881036, 'cguzman036@estudiante.edu', 'Activo', 'CAR-036', 'CUR-CNT', 102, 202601, 'Aula 201', 'Miércoles', '13:00:00', '16:00:00'),
('EST-037', 'Esteban', 'Pacheco', 88881037, 'epacheco037@estudiante.edu', 'Activo', 'CAR-037', 'CUR-ISW', 102, 202601, 'Lab 2', 'Jueves', '08:00:00', '11:00:00'),
('EST-038', 'Monica', 'Calvo', 88881038, 'mcalvo038@estudiante.edu', 'Inactivo', 'CAR-038', 'CUR-CNT', 102, 202601, 'Aula 201', 'Miércoles', '13:00:00', '16:00:00'),
('EST-039', 'Sebastian', 'Zamora', 88881039, 'szamora039@estudiante.edu', 'Activo', 'CAR-039', 'CUR-BD1', 101, 202601, 'Lab 3', 'Lunes', '08:00:00', '11:00:00'),
('EST-040', 'Gabriela', 'Brenes', 88881040, 'gbrenes040@estudiante.edu', 'Activo', 'CAR-040', 'CUR-BD2', 101, 202601, 'Lab 3', 'Viernes', '08:00:00', '11:00:00'),
('EST-041', 'Felipe', 'Villalobos', 88881041, 'fvillalobos041@estudiante.edu', 'Activo', 'CAR-041', 'CUR-BD1', 101, 202601, 'Lab 3', 'Lunes', '08:00:00', '11:00:00'),
('EST-042', 'Adriana', 'Orozco', 88881042, 'aorozco042@estudiante.edu', 'Inactivo', 'CAR-042', 'CUR-IA', 102, 202601, 'Lab 4', 'Sábado', '13:00:00', '17:00:00'),
('EST-043', 'Mario', 'Quesada', 88881043, 'mquesada043@estudiante.edu', 'Activo', 'CAR-043', 'CUR-BD1', 101, 202601, 'Lab 3', 'Lunes', '08:00:00', '11:00:00'),
('EST-044', 'Lorena', 'Romero', 88881044, 'lromero044@estudiante.edu', 'Activo', 'CAR-044', 'CUR-CNT', 102, 202601, 'Aula 201', 'Miércoles', '13:00:00', '16:00:00'),
('EST-045', 'Gonzalo', 'Miranda', 88881045, 'gmiranda045@estudiante.edu', 'Activo', 'CAR-045', 'CUR-CIB', 101, 202601, 'Lab 1', 'Lunes', '13:00:00', '16:00:00'),
('EST-046', 'Verónica', 'Fonseca', 88881046, 'vfonseca046@estudiante.edu', 'Inactivo', 'CAR-046', 'CUR-CNT', 102, 202601, 'Aula 201', 'Miércoles', '13:00:00', '16:00:00'),
('EST-047', 'Oscar', 'Porras', 88881047, 'oporras047@estudiante.edu', 'Activo', 'CAR-047', 'CUR-BD1', 101, 202601, 'Lab 3', 'Lunes', '08:00:00', '11:00:00'),
('EST-048', 'Andrea', 'Madrigal', 88881048, 'amadrigal048@estudiante.edu', 'Activo', 'CAR-048', 'CUR-WEB', 102, 202601, 'Lab 2', 'Martes', '18:00:00', '21:00:00'),
('EST-049', 'Francisco', 'Solís', 88881049, 'fsolis049@estudiante.edu', 'Activo', 'CAR-049', 'CUR-BD1', 101, 202601, 'Lab 3', 'Lunes', '08:00:00', '11:00:00'),
('EST-050', 'Karla', 'Valverde', 88881050, 'kvalverde050@estudiante.edu', 'Inactivo', 'CAR-050', 'CUR-MOV', 101, 202601, 'Lab 3', 'Miércoles', '18:00:00', '21:00:00');

---Insertar Base de datos facultad ---
INSERT INTO dbo.facultad (facultad_id, nombre_facultad, edificio, decano) VALUES
('FAC-ING', 'Facultad de Ingeniería', 'Edificio A', 'Dr. Roberto Gómez'),
('FAC-CED', 'Facultad de Ciencias Económicas', 'Edificio C','Dra. María Fernández'),
('FAC-SAL', 'Facultad de Ciencias de la Salud', 'Edificio C', 'MSc. Jorge Ramírez'),
('FAC-DER', 'Facultad de Derecho y Ciencias Políticas', 'Edificio D', 'Licda. Sofia Castro'),
('FAC-EDU', 'Facultad de Educación y Humanidades', 'Edificio E', 'MSc. Jorge Ramírez');



---Insertar Base de datos curso---
INSERT INTO dbo.curso (curso_id, nombre_curso, credito_del_curso) VALUES
('CUR-BD1', 'Bases de Datos I', 4),
('CUR-CNT', 'Contabilidad General', 3),
('CUR-PRO', 'Programación Orientada a Objetos', 4),
('CUR-MAT', 'Cálculo Diferencial', 4),
('CUR-DER', 'Derecho Constitucional', 3),
('CUR-ADM', 'Principios de Administración', 3),
('CUR-MED', 'Anatomía Humana', 5),
('CUR-EDU', 'Pedagogía General', 3),
('CUR-EST', 'Estadística Descriptiva', 4),
('CUR-MKT', 'Fundamentos de Mercadeo', 3),
('CUR-ALG', 'Álgebra Lineal', 4),
('CUR-CAL2', 'Cálculo Multivariable', 4),
('CUR-EDO', 'Ecuaciones Diferenciales', 4),
('CUR-ISW', 'Ingeniería de Software', 4),
('CUR-BD2', 'Bases de Datos II', 4),
('CUR-IA', 'Inteligencia Artificial', 4),
('CUR-CIB', 'Ciberseguridad Básica', 3),
('CUR-WEB', 'Desarrollo Web Integrado', 3),
('CUR-MOV', 'Desarrollo de Aplicaciones Móviles', 3),
('CUR-MAC', 'Macroeconomía', 3),
('CUR-CON2', 'Contabilidad de Costos', 3),
('CUR-AUD', 'Auditoría Financiera', 3),
('CUR-MER2', 'Investigación de Mercados', 3),
('CUR-ARQ', 'Arquitectura de Computadoras', 4),
('CUR-EMP', 'Emprendimiento y Creación de Empresas', 2),
('CUR-GPR', 'Gestión de Proyectos', 3),
('CUR-DTR', 'Derecho del Trabajo', 3),
('CUR-DME', 'Derecho Mercantil', 3),
('CUR-FARM', 'Farmacología General', 4),
('CUR-PAT', 'Patología Médica', 5),
('CUR-FISIO', 'Fisiología Humana', 5),
('CUR-BIOQ', 'Bioquímica Clínica', 4),
('CUR-GEN', 'Genética General', 4),
('CUR-SOC', 'Sociología Contemporánea', 3),
('CUR-HIS', 'Historia Universal', 3);


---Insertar la base de datos de profesor

INSERT INTO dbo.profesor (profesor_id, nombre, apellido, email, nombre_curso) VALUES
(101, 'Alberto', 'Morales', 'amorales@universidad.edu', 'Bases de Datos I'),
(102, 'Sonia', 'Gutiérrez', 'sgutierrez@universidad.edu', 'Contabilidad General'),
(103, 'Ricardo', 'Alvarado', 'ralvarado@universidad.edu', 'Bases de Datos I'),
(104, 'Mónica', 'Fernández', 'mfernandez@universidad.edu', 'Programación Orientada a Objetos'),
(105, 'Esteban', 'Chaves', 'echaves@universidad.edu', 'Cálculo Diferencial'),
(106, 'Lucía', 'Mora', 'lmora@universidad.edu', 'Derecho Constitucional'),
(107, 'Fernando', 'Zamora', 'fzamora@universidad.edu', 'Principios de Administración'),
(108, 'Beatriz', 'Solano', 'bsolano@universidad.edu', 'Anatomía Humana'),
(109, 'Jorge', 'Pacheco', 'jpacheco@universidad.edu', 'Pedagogía General'),
(110, 'Patricia', 'Araya', 'paraya@universidad.edu', 'Estadística Descriptiva'),
(111, 'Roberto', 'Brenes', 'rbrenes@universidad.edu', 'Bases de Datos I'),
(112, 'Gabriela', 'Campos', 'gcampos@universidad.edu', 'Contabilidad General'),
(113, 'Felipe', 'Vargas', 'fvargas@universidad.edu', 'Programación Orientada a Objetos'),
(114, 'Adriana', 'Rojas', 'arojas@universidad.edu', 'Cálculo Diferencial'),
(115, 'Mario', 'Jiménez', 'mjimenez@universidad.edu', 'Cálculo Diferencial'),
(116, 'Lorena', 'Castro', 'lcastro@universidad.edu', 'Ingeniería de Software'),
(117, 'Gonzalo', 'Pérez', 'gperez@universidad.edu', 'Programación Orientada a Objetos'),
(118, 'Verónica', 'Gómez', 'vgomez@universidad.edu', 'Inteligencia Artificial'),
(119, 'Oscar', 'López', 'olopez@universidad.edu', 'Derecho Constitucional'),
(120, 'Andrea', 'Sánchez', 'asanchez@universidad.edu', 'Desarrollo Web Integrado'),
(121, 'Francisco', 'Torres', 'ftorres@universidad.edu', 'Ingeniería de Software'),
(122, 'Karla', 'Ramírez', 'kramirez@universidad.edu', 'Principios de Administración'),
(123, 'Diego', 'Mendoza', 'dmendoza@universidad.edu', 'Contabilidad General'),
(124, 'Elena', 'Herrera', 'eherrera@universidad.edu', 'Estadística Descriptiva'),
(125, 'Gabriel', 'Aguilar', 'gaguilar@universidad.edu', 'Fundamentos de Mercadeo'),
(126, 'Mateo', 'Navarro', 'mnavarro@universidad.edu', 'Inteligencia Artificial'),
(127, 'Paula', 'Vega', 'pvega@universidad.edu', 'Fundamentos de Mercadeo'),
(128, 'Andrés', 'Cordero', 'acordero@universidad.edu', 'Principios de Administración'),
(129, 'Camila', 'Blanco', 'cblanco@universidad.edu', 'Derecho Constitucional'),
(130, 'Javier', 'Soto', 'jsoto@universidad.edu', 'Estadística Descriptiva'),
(131, 'Valeria', 'Orozco', 'vorozco@universidad.edu', 'Anatomía Humana'),
(132, 'Daniel', 'Quesada', 'dquesada@universidad.edu', 'Pedagogía General'),
(133, 'Mariana', 'Romero', 'mromero@universidad.edu', 'Anatomía Humana'),
(134, 'Alejandro', 'Miranda', 'amiranda@universidad.edu', 'Desarrollo Web Integrado'),
(135, 'Natalia', 'Fonseca', 'nfonseca@universidad.edu', 'Pedagogía General');

---Insert de base de datos de matricula

INSERT INTO dbo.matricula (matricula_id, estudiante_id, curso_id, fecha_registro) VALUES
('MAT-001', 'EST-001', 'CUR-BD1', '2025-12-01'),
('MAT-002', 'EST-002', 'CUR-CNT', '2025-12-03'),
('MAT-003', 'EST-003', 'CUR-BD1', '2025-12-05'),
('MAT-004', 'EST-004', 'CUR-CNT', '2025-12-10'),
('MAT-005', 'EST-005', 'CUR-BD1', '2025-12-12'),
('MAT-006', 'EST-006', 'CUR-PRO', '2025-12-15'),
('MAT-007', 'EST-007', 'CUR-BD1', '2025-12-18'),
('MAT-008', 'EST-008', 'CUR-CNT', '2025-12-20'),
('MAT-009', 'EST-009', 'CUR-MAT', '2026-01-02'),
('MAT-010', 'EST-010', 'CUR-CNT', '2026-01-03'),
('MAT-011', 'EST-011', 'CUR-BD1', '2026-01-05'),
('MAT-012', 'EST-012', 'CUR-DER', '2026-01-07'),
('MAT-013', 'EST-013', 'CUR-BD1', '2026-01-08'),
('MAT-014', 'EST-014', 'CUR-CNT', '2026-01-10'),
('MAT-015', 'EST-015', 'CUR-BD1', '2026-01-12'),
('MAT-016', 'EST-016', 'CUR-ADM', '2026-01-14'),
('MAT-017', 'EST-017', 'CUR-BD1', '2026-01-15'),
('MAT-018', 'EST-018', 'CUR-CNT', '2026-01-16'),
('MAT-019', 'EST-019', 'CUR-MED', '2026-01-18'),
('MAT-020', 'EST-020', 'CUR-CNT', '2026-01-19'),
('MAT-021', 'EST-021', 'CUR-BD1', '2026-01-20'),
('MAT-022', 'EST-022', 'CUR-EDU', '2026-01-21'),
('MAT-023', 'EST-023', 'CUR-BD1', '2026-01-22'),
('MAT-024', 'EST-024', 'CUR-CNT', '2026-01-23'),
('MAT-025', 'EST-025', 'CUR-EST', '2026-01-24'),
('MAT-026', 'EST-026', 'CUR-CNT', '2026-01-25'),
('MAT-027', 'EST-027', 'CUR-BD1', '2026-01-26'),
('MAT-028', 'EST-028', 'CUR-MKT', '2026-01-27'),
('MAT-029', 'EST-029', 'CUR-BD1', '2026-01-28'),
('MAT-030', 'EST-030', 'CUR-CNT', '2026-01-29'),
('MAT-031', 'EST-031', 'CUR-ALG', '2026-01-30'),
('MAT-032', 'EST-032', 'CUR-CNT', '2026-01-31'),
('MAT-033', 'EST-033', 'CUR-BD1', '2026-02-01'),
('MAT-034', 'EST-034', 'CUR-CAL2', '2026-02-02'),
('MAT-035', 'EST-035', 'CUR-BD1', '2026-02-03'),
('MAT-036', 'EST-036', 'CUR-CNT', '2026-02-04'),
('MAT-037', 'EST-037', 'CUR-ISW', '2026-02-05'),
('MAT-038', 'EST-038', 'CUR-CNT', '2026-02-06'),
('MAT-039', 'EST-039', 'CUR-BD1', '2026-02-07'),
('MAT-040', 'EST-040', 'CUR-BD2', '2026-02-08'),
('MAT-041', 'EST-041', 'CUR-BD1', '2026-02-09'),
('MAT-042', 'EST-042', 'CUR-IA', '2026-02-10'),
('MAT-043', 'EST-043', 'CUR-BD1', '2026-02-11'),
('MAT-044', 'EST-044', 'CUR-CNT', '2026-02-12'),
('MAT-045', 'EST-045', 'CUR-WEB', '2026-02-13'),
('MAT-046', 'EST-046', 'CUR-CNT', '2026-02-14'),
('MAT-047', 'EST-047', 'CUR-BD1', '2026-02-15'),
('MAT-048', 'EST-048', 'CUR-MOV', '2026-02-16'),
('MAT-049', 'EST-049', 'CUR-BD1', '2026-02-17'),
('MAT-050', 'EST-050', 'CUR-MAC', '2026-02-18');

insert into dbo.detalle_matricula (
    matricula_id, periodo_id, estado_curso, nombre_periodo, fecha_inicio, fecha_fin
) values
('MAT-001', 202601, 'activo', 'I Semestre 2026', '2026-01-12', '2026-06-26'),
('MAT-002', 202601, 'activo', 'I Semestre 2026', '2026-01-12', '2026-06-26'),
('MAT-003', 202601, 'inactivo', 'I Semestre 2026', '2026-01-12', '2026-06-26'),
('MAT-004', 202601, 'activo', 'I Semestre 2026', '2026-01-12', '2026-06-26'),
('MAT-005', 202601, 'inactivo', 'I Semestre 2026', '2026-01-12', '2026-06-26'),
('MAT-006', 202601, 'inactivo', 'I Semestre 2026', '2026-01-12', '2026-06-26'),
('MAT-007', 202601, 'activo', 'I Semestre 2026', '2026-01-12', '2026-06-26'),
('MAT-008', 202601, 'inactivo', 'I Semestre 2026', '2026-01-12', '2026-06-26'),
('MAT-009', 202601, 'activo', 'I Semestre 2026', '2026-01-12', '2026-06-26'),
('MAT-010', 202601, 'inactivo', 'I Semestre 2026', '2026-01-12', '2026-06-26'),
('MAT-011', 202601, 'activo', 'I Semestre 2026', '2026-01-12', '2026-06-26'),
('MAT-012', 202601, 'inactivo', 'I Semestre 2026', '2026-01-12', '2026-06-26'),
('MAT-013', 202601, 'activo', 'I Semestre 2026', '2026-01-12', '2026-06-26'),
('MAT-014', 202601, 'activo', 'I Semestre 2026', '2026-01-12', '2026-06-26'),
('MAT-015', 202601, 'activo', 'I Semestre 2026', '2026-01-12', '2026-06-26'),
('MAT-016', 202601, 'inactivo', 'I Semestre 2026', '2026-01-12', '2026-06-26'),
('MAT-017', 202601, 'activo', 'I Semestre 2026', '2026-01-12', '2026-06-26'),
('MAT-018', 202601, 'inactivo', 'I Semestre 2026', '2026-01-12', '2026-06-26'),
('MAT-019', 202601, 'activo', 'I Semestre 2026', '2026-01-12', '2026-06-26'),
('MAT-020', 202601, 'inactivo', 'I Semestre 2026', '2026-01-12', '2026-06-26'),
('MAT-021', 202601, 'activo', 'I Semestre 2026', '2026-01-12', '2026-06-26'),
('MAT-022', 202601, 'activo', 'I Semestre 2026', '2026-01-12', '2026-06-26'),
('MAT-023', 202601, 'activo', 'I Semestre 2026', '2026-01-12', '2026-06-26'),
('MAT-024', 202601, 'inactivo', 'I Semestre 2026', '2026-01-12', '2026-06-26'),
('MAT-025', 202601, 'inactivo', 'I Semestre 2026', '2026-01-12', '2026-06-26'),
('MAT-026', 202601, 'activo', 'I Semestre 2026', '2026-01-12', '2026-06-26'),
('MAT-027', 202601, 'activo', 'I Semestre 2026', '2026-01-12', '2026-06-26'),
('MAT-028', 202601, 'activo', 'I Semestre 2026', '2026-01-12', '2026-06-26'),
('MAT-029', 202601, 'inactivo', 'I Semestre 2026', '2026-01-12', '2026-06-26'),
('MAT-030', 202601, 'activo', 'I Semestre 2026', '2026-01-12', '2026-06-26'),
('MAT-031', 202601, 'activo', 'I Semestre 2026', '2026-01-12', '2026-06-26'),
('MAT-032', 202601, 'inactivo', 'I Semestre 2026', '2026-01-12', '2026-06-26'),
('MAT-033', 202601, 'activo', 'I Semestre 2026', '2026-01-12', '2026-06-26'),
('MAT-034', 202601, 'inactivo', 'I Semestre 2026', '2026-01-12', '2026-06-26'),
('MAT-035', 202601, 'activo', 'I Semestre 2026', '2026-01-12', '2026-06-26'),
('MAT-036', 202601, 'activo', 'I Semestre 2026', '2026-01-12', '2026-06-26'),
('MAT-037', 202601, 'activo', 'I Semestre 2026', '2026-01-12', '2026-06-26'),
('MAT-038', 202601, 'inactivo', 'I Semestre 2026', '2026-01-12', '2026-06-26'),
('MAT-039', 202601, 'activo', 'I Semestre 2026', '2026-01-12', '2026-06-26'),
('MAT-040', 202601, 'inactivo', 'I Semestre 2026', '2026-01-12', '2026-06-26'),
('MAT-041', 202601, 'activo', 'I Semestre 2026', '2026-01-12', '2026-06-26'),
('MAT-042', 202601, 'activo', 'I Semestre 2026', '2026-01-12', '2026-06-26'),
('MAT-043', 202601, 'activo', 'I Semestre 2026', '2026-01-12', '2026-06-26'),
('MAT-044', 202601, 'inactivo', 'I Semestre 2026', '2026-01-12', '2026-06-26'),
('MAT-045', 202601, 'activo', 'I Semestre 2026', '2026-01-12', '2026-06-26'),
('MAT-046', 202601, 'activo', 'I Semestre 2026', '2026-01-12', '2026-06-26'),
('MAT-047', 202601, 'activo', 'I Semestre 2026', '2026-01-12', '2026-06-26'),
('MAT-048', 202601, 'inactivo', 'I Semestre 2026', '2026-01-12', '2026-06-26'),
('MAT-049', 202601, 'activo', 'I Semestre 2026', '2026-01-12', '2026-06-26'),
('MAT-050', 202601, 'activo', 'I Semestre 2026', '2026-01-12', '2026-06-26'),
('MAT-051', 202502, 'inactivo', 'II Semestre 2025', '2025-07-14', '2025-12-19'),
('MAT-052', 202502, 'inactivo', 'II Semestre 2025', '2025-07-14', '2025-12-19');


---insercion de datos a la base de datos pago ---

INSERT INTO dbo.pago (matricula_id, monto, fecha_pago, metodo_pago) VALUES
('MAT-001', 150000.00, '2025-12-01', 'Tarjeta de Crédito'),
('MAT-002', 125000.00, '2025-12-03', 'Transferencia'),
('MAT-003', 150000.00, '2025-12-05', 'Efectivo'),
('MAT-004', 125000.00, '2025-12-10', 'SINPE Movil'),
('MAT-005', 150000.00, '2025-12-12', NULL),
('MAT-006', 135000.00, '2025-12-15', 'Tarjeta de Débito'),
('MAT-007', 150000.00, '2025-12-18', 'Transferencia'),
('MAT-008', 125000.00, '2025-12-20', 'Efectivo'),
('MAT-009', 140000.00, '2026-01-02', 'SINPE Movil'),
('MAT-010', 125000.00, '2026-01-03', 'Tarjeta de Crédito'),
('MAT-011', 150000.00, '2026-01-05', NULL),
('MAT-012', 160000.00, '2026-01-07', 'Transferencia'),
('MAT-013', 150000.00, '2026-01-08', 'SINPE Movil'),
('MAT-014', 125000.00, '2026-01-10', 'Tarjeta de Débito'),
('MAT-015', 150000.00, '2026-01-12', 'Efectivo'),
('MAT-016', 130000.00, '2026-01-14', 'Transferencia'),
('MAT-017', 150000.00, '2026-01-15', 'Tarjeta de Crédito'),
('MAT-018', 125000.00, '2026-01-16', NULL),
('MAT-019', 180000.00, '2026-01-18', 'Transferencia'),
('MAT-020', 125000.00, '2026-01-19', 'SINPE Movil'),
('MAT-021', 150000.00, '2026-01-20', 'Efectivo'),
('MAT-022', 135000.00, '2026-01-21', 'Tarjeta de Débito'),
('MAT-023', 150000.00, '2026-01-22', 'Transferencia'),
('MAT-024', 125000.00, '2026-01-23', 'Tarjeta de Crédito'),
('MAT-025', 140000.00, '2026-01-24', NULL),
('MAT-026', 125000.00, '2026-01-25', 'SINPE Movil'),
('MAT-027', 150000.00, '2026-01-26', 'Transferencia'),
('MAT-028', 145000.00, '2026-01-27', 'Tarjeta de Crédito'),
('MAT-029', 150000.00, '2026-01-28', 'Efectivo'),
('MAT-030', 125000.00, '2026-01-29', 'Transferencia'),
('MAT-031', 135000.00, '2026-01-30', 'SINPE Movil'),
('MAT-032', 125000.00, '2026-01-31', 'Tarjeta de Débito'),
('MAT-033', 150000.00, '2026-02-01', NULL),
('MAT-034', 155000.00, '2026-02-02', 'Transferencia'),
('MAT-035', 150000.00, '2026-02-03', 'Tarjeta de Crédito'),
('MAT-036', 125000.00, '2026-02-04', 'SINPE Movil'),
('MAT-037', 165000.00, '2026-02-05', 'Efectivo'),
('MAT-038', 125000.00, '2026-02-06', 'Transferencia'),
('MAT-039', 150000.00, '2026-02-07', 'Tarjeta de Débito'),
('MAT-040', 150000.00, '2026-02-08', 'Tarjeta de Crédito'),
('MAT-041', 150000.00, '2026-02-09', NULL),
('MAT-042', 170000.00, '2026-02-10', 'SINPE Movil'),
('MAT-043', 150000.00, '2026-02-11', 'Transferencia'),
('MAT-044', 125000.00, '2026-02-12', 'Efectivo'),
('MAT-045', 140000.00, '2026-02-13', 'Tarjeta de Crédito'),
('MAT-046', 125000.00, '2026-02-14', 'SINPE Movil'),
('MAT-047', 150000.00, '2026-02-15', 'Transferencia'),
('MAT-048', 145000.00, '2026-02-16', 'Tarjeta de Débito'),
('MAT-049', 150000.00, '2026-02-17', NULL),
('MAT-050', 135000.00, '2026-02-18', 'Transferencia');


---Entrada de datos de base de datos factura---
 
INSERT INTO dbo.factura (estudiante_id, fecha_emision, monto_total) VALUES

('EST-001', '2025-12-01', 150000),
('EST-002', '2025-12-03', 125000),
('EST-003', '2025-12-05', 150000),
('EST-004', '2025-12-10', 125000),
('EST-005', '2025-12-12', 150000),
('EST-006', '2025-12-15', 135000),
('EST-007', '2025-12-18', 150000),
('EST-008', '2025-12-20', 125000),
('EST-009', '2026-01-02', 140000),
('EST-010', '2026-01-03', 125000),
('EST-011', '2026-01-05', 150000),
('EST-012', '2026-01-07', 160000),
('EST-013', '2026-01-08', 150000),
('EST-014', '2026-01-10', 125000),
('EST-015', '2026-01-12', 150000),
('EST-016', '2026-01-14', 130000),
('EST-017', '2026-01-15', 150000),
('EST-018', '2026-01-16', 125000),
('EST-019', '2026-01-18', 180000),
('EST-020', '2026-01-19', 125000),
('EST-021', '2026-01-20', 150000),
('EST-022', '2026-01-21', 135000),
('EST-023', '2026-01-22', 150000),
('EST-024', '2026-01-23', 125000),
('EST-025', '2026-01-24', 140000),
('EST-026', '2026-01-25', 125000),
('EST-027', '2026-01-26', 150000),
('EST-028', '2026-01-27', 145000),
('EST-029', '2026-01-28', 150000),
('EST-030', '2026-01-29', 125000),
('EST-031', '2026-01-30', 135000),
('EST-032', '2026-01-31', 125000),
('EST-033', '2026-02-01', 150000),
('EST-034', '2026-02-02', 155000),
('EST-035', '2026-02-03', 150000),
('EST-036', '2026-02-04', 125000),
('EST-037', '2026-02-05', 165000),
('EST-038', '2026-02-06', 125000),
('EST-039', '2026-02-07', 150000),
('EST-040', '2026-02-08', 150000),
('EST-041', '2026-02-09', 150000),
('EST-042', '2026-02-10', 170000),
('EST-043', '2026-02-11', 150000),
('EST-044', '2026-02-12', 125000),
('EST-045', '2026-02-13', 140000),
('EST-046', '2026-02-14', 125000),
('EST-047', '2026-02-15', 150000),
('EST-048', '2026-02-16', 145000),
('EST-049', '2026-02-17', 150000),
('EST-050', '2026-02-18', 135000);



