Use proyecto_final_mpd
-- Consultas de selección para cada tabla

SELECT * FROM dbo.facultad;
SELECT * FROM dbo.carrera;
SELECT * FROM dbo.profesor;
SELECT * FROM dbo.estudiante;
SELECT * FROM dbo.curso;
SELECT * FROM dbo.matricula;
SELECT * FROM dbo.detalle_matricula;
SELECT * FROM dbo.pago;
SELECT * FROM dbo.factura;

----SELECT
---Consultar select toda la tabla de carrera ademas la lista general de carreras y filtrar campos específicos
select * from carrera;
select carrera_id, titulo_otorgado from carrera;

----WHERE
---Filtrar los estudiantes matriculados en un curso específico
select estudiante_id, curso_id from matricula
where curso_id = 'CUR-BD1';

----ORDER BY
---Obtener las clases de los lunes ordenadas cronológicamente por hora de inicio
select curso_id, hora_inicio, periodo_id from estudiante
where dia_semana = 'lunes'
order by hora_inicio asc;

----DISTINCT
---Listar combinaciones únicas de cursos y profesores ordenados alfabéticamente de forma descendente
select distinct nombre_curso, profesor_id, nombre, apellido from profesor
order by nombre_curso desc;

----TOP
---Obtener las primeras 5 carreras con duración de 10 o más semestres
select top 5 carrera_id, duracion_semestre from carrera
where duracion_semestre >= 10
order by titulo_otorgado desc;

----LIKE
---Obtener los 2 montos de factura más altos registrados
select top 2 estudiante_id, monto_total from factura
order by monto_total desc;

----BETWEEN
---Buscar los 10 montos de factura más altos que estén dentro del rango de 150,000 a 170,000
select top 10 estudiante_id, monto_total from factura 
where monto_total between 150000 and 170000
order by monto_total desc;

----IN
---Consultar detalles de matrícula que coincidan con una lista específica de identificadores
select * from detalle_matricula
where detalle_id IN (12020, 12025, 12029);

----NOT
---Filtrar facultades excluyendo 'Ciencias Económicas' y 'Ciencias de la Salud'
select * from facultad
where not nombre_facultad in ('Facultad de Ciencias Económicas', 'Facultad de Ciencias de la Salud');

----IS NULL
---Buscar los registros de pago que no tienen un método de pago registrado
select * from pago
where metodo_pago is null;

----IS NOT NULL
---Consultar los pagos que sí cuentan con un método de pago asignado
select * from pago
where metodo_pago is not null;

----AND
---Buscar pagos realizados en enero de 2026 and que usaron 'SINPE Movil'
select pago_id, matricula_id, monto, fecha_pago, metodo_pago from pago
where fecha_pago >= '2026-01-01' and metodo_pago = 'SINPE Movil';

----OR
---Buscar pagos realizados en enero de 2026 or que usaron 'SINPE Movil'
select pago_id, matricula_id, monto, fecha_pago, metodo_pago from pago
where fecha_pago <= '2026-01-01' or metodo_pago = 'SINPE Movil';

----GROUP BY
-- Agrupar los pagos por método de pago para ver el total cobrado y la cantidad de pagos por cada método
select  metodo_pago,sum(monto) as Totales_de_Metodo_de_pago from pago
group by metodo_pago;

----HAVING
---Obtener el monto total agrupado por método de pago donde la suma supere los 1,200,000
select metodo_pago, sum(monto) as Totales_de_Metodo_de_pago 
from pago
group by metodo_pago
having sum(monto) > 1200000;

----COUNT
---Contar el total de estudiantes inscritos agrupados por cada curso
select curso_id, count(estudiante_id) AS total_estudiantes 
from estudiante
where curso_id is not null
group by curso_id;

----SUM
---Calcular la suma total del monto pagado para cada método de pago registrado
select metodo_pago, sum(monto) as Totales_de_Metodo_de_pago 
from pago
where metodo_pago is not null
group by metodo_pago;

--- Obtener el monto promedio total de las facturas emitidas
select AVG(monto_total) as promedio_monto_factura from dbo.factura;
----MIN
--- Calcular la duración minimo (en semestres) de todas las carreras
select min(duracion_semestre) as el_miniimo_duracion_por_semestres from carrera;
----MAX
--- Calcular la duración maximo (en semestres) de todas las carreras
select max(duracion_semestre) as el_maximo_duracion_por_semestres from carrera;
----INNER JOIN
select * from carrera c
inner join estudiante e
on c.carrera_id = e.carrera_id;

----LEFT JOIN

select p.profesor_id,p.nombre, e.curso_id from dbo.profesor p
left join dbo.estudiante e 
on p.profesor_id = e.profesor_id;
    
    ---Right JOIN
select * from dbo.matricula m
right join dbo.estudiante e 
on m.estudiante_id = e.estudiante_id;
----Subconsultas

select p.pago_id,p.matricula_id,p.monto FROM pago p
where p.monto > (select avg(monto) from pago
);
go
----CREATE VIEW (Vistas)
CREATE VIEW profesor_estudiante AS 
SELECT DISTINCT p.profesor_id,p.nombre AS nombre_profesor,e.curso_id FROM dbo.profesor p
LEFT JOIN dbo.estudiante e ON p.profesor_id = e.profesor_id;
GO



---   1. VISTA: estudiantes_horarios

-- Enseña el horario de clases de los estudiantes junto con su curso
-- para ayudar a la administración a consultar la agenda sin hacer búsquedas complejas.

CREATE VIEW estudiantes_horarios AS
SELECT e.estudiante_id,CONCAT(e.nombre, ' ', e.apellido) AS nombre_estudiante,c.nombre_curso,e.aula,e.dia_semana,e.hora_inicio,e.hora_fin
FROM estudiante e
INNER JOIN curso c ON e.curso_id = c.curso_id;
GO



  --- 2. VISTA: resumen_facturacion_estudiante
-- Muestra el total facturado a cada estudiante
-- para ayudar al departamento de cobros a llevar un control financiero rápido.

create view resumen_facturacion_estudiante as
select e.estudiante_id,e.nombre,e.apellido, sum(f.monto_total) as total_facturado from estudiante e
left join factura f on e.estudiante_id = f.estudiante_id
group by e.estudiante_id, e.nombre, e.apellido;
go

--3. VISTA: estudiantes_actividad_carrera

---Con esta vista ayuda a mostrar cuántos estudiantes están activos e inactivos por cada carrera
-- ademas ayuda a la administración a identificar carreras con riesgo de deserción.
create view estudiantes_actividad_carrera as
select c.titulo_otorgado,e.estado_de_actividad,count(e.estudiante_id) as total_estudiantes from carrera c
INNER JOIN estudiante e on c.carrera_id = e.carrera_id
group by c.titulo_otorgado, e.estado_de_actividad;
go



---4. VISTA: ocupacion_cursos

-- Se muestra la cantidad de estudiantes matriculados por curso
-- para ayudar a la administración a controlar la cantidad de estudiantes por curso.

create view ocupacion_cursos as
select c.curso_id,c.nombre_curso,count(e.estudiante_id) as cantidad_estudiantes from curso c
left join  estudiante e on c.curso_id = e.curso_id
group by c.curso_id, c.nombre_curso;
go


---5. VISTA: profesor_estudiante
-- Muestra que profesores le imparten clase a qué estudiantes
-- Ayuda controlar mas el ritmo estudiante a porfesor

create view profesor_estudiante as
select distinct p.profesor_id,concat(p.nombre, ' ', p.apellido) AS nombre_profesor,e.estudiante_id,concat(e.nombre, ' ', e.apellido) as nombre_estudiante
from profesor p
inner join estudiante e on p.profesor_id = e.profesor_id;
go

---6. VISTA: auditoria_matricula_periodo
-- Esta tabla es para mostrar el historial de la matricula en conjunto con el periodo lectivo 
--para ayudar a realizar una auditoría de cómo va el semestre.

create view auditoria_matricula_periodo as
select m.matricula_id,m.fecha_registro as fecha_matricula,dm.nombre_periodo,dm.estado_curso,dm.fecha_inicio,dm.fecha_fin
from matricula m
inner join detalle_matricula dm on m.matricula_id = dm.matricula_id;
go

