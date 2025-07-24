# ¿Cómo crear un repositorio remoto en GitHub y sincronizarlo con el repositorio local?

Para trabajar con un repositorio remoto en GitHub y sincronizarlo con tu repositorio local, sigue estos pasos:

1. **Crea el repositorio en GitHub:**
   - Ingresa a **https://github.com** y accede a tu cuenta.
   - Haz clic en "New" o "Nuevo repositorio".
   - Escribe el nombre del repositorio y configura las opciones deseadas.
   - Haz clic en "Create repository".

2. **Obtén la URL del repositorio remoto:**
   - Copia la URL que aparece **https://github.com/usuario/nombre-repo.git**.

3. **Vincula tu repositorio local con el remoto:**
   - Abre la terminal y navega a la carpeta de tu proyecto local.
   - Ejecuta el siguiente comando, reemplazando la URL por la de tu repositorio:
     git remote add origin **https://github.com/usuario/nombre-repo.git**

4. **Envía tus cambios locales al repositorio remoto:**
   - Sube tu rama principal (por lo general llamada **main** o **master**) con:
     git push -u origin main
   - Si tu rama se llama **master**, reemplaza **main** por **master**.

¡Listo! Ahora tu repositorio local está sincronizado con GitHub y puedes compartir tu proyecto o colaborar con otros.