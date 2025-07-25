# Cómo crear y sincronizar un repositorio remoto en GitHub

Un repositorio remoto es una copia de tu proyecto almacenada en la nube, por ejemplo, en GitHub. Esto permite compartir tu código y colaborar con otras personas. A continuación, se detalla el proceso para crear un repositorio remoto y sincronizarlo con tu repositorio local.

## Pasos para crear y sincronizar un repositorio remoto

1. **Crea un repositorio en GitHub:**
   - Ingresa a [github.com](https://github.com/) y accede con tu cuenta.
   - Haz clic en el botón **"New"** o **"Nuevo repositorio"**.
   - Escribe el nombre del repositorio y una descripción (opcional).
   - Elige si será público o privado.
   - Haz clic en **"Create repository"**.

2. **Vincula tu repositorio local con el remoto:**
   - Copia la URL del repositorio que aparece en GitHub (por ejemplo: `https://github.com/usuario/nombre-repo.git`).
   - En la consola, dentro de la carpeta de tu proyecto local, ejecuta:
     ```sh
     git remote add origin https://github.com/usuario/nombre-repo.git
     ```

3. **Sube tu proyecto local a GitHub:**
   - Si es la primera vez que subes el proyecto, usa:
     ```sh
     git branch -M main
     git push -u origin main
     ```
   - Para subir cambios en el futuro, solo necesitas:
     ```sh
     git push
     ```

## Resumen de comandos

- `git remote add origin <url>` — Vincula el repositorio local con el remoto.
- `git branch -M main` — Cambia el nombre de la rama principal a "main".
- `git push -u origin main` — Sube el contenido local a GitHub y establece la rama principal.
- `git push` — Sube cambios futuros al repositorio remoto.

Con estos pasos, tu repositorio local y remoto estarán sincronizados y listos para trabajar en equipo o desde