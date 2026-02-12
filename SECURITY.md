# Política de Seguridad

## Reportando una Vulnerabilidad

Si descubres una vulnerabilidad de seguridad en nanobot, por favor repórtala de la siguiente manera:

1. **NO** abras un issue público en GitHub.
2. Crea un aviso de seguridad privado en GitHub o contacta a los mantenedores del repositorio.
3. Incluye:
   - Descripción de la vulnerabilidad
   - Pasos para reproducirla
   - Impacto potencial
   - Solución sugerida (si la hay)

Nos esforzamos por responder a los reportes de seguridad dentro de 48 horas.

## Mejores Prácticas de Seguridad

### 1. Gestión de Claves API

**CRÍTICO**: Nunca hagas commit de claves API al control de versiones.

```bash
# ✅ Bien: Almacenar en archivo de configuración con permisos restringidos
chmod 600 ~/.nanobot/config.json

# ❌ Mal: Hardcodear claves en código o hacerles commit
```

**Recomendaciones:**
- Almacena claves API en `~/.nanobot/config.json` con permisos de archivo establecidos a `0600`
- Considera usar variables de entorno para claves sensibles
- Usa el gestor de credenciales/keyring del SO para despliegues en producción
- Rota las claves API regularmente
- Usa claves API separadas para desarrollo y producción

### 2. Control de Acceso a Canales

**IMPORTANTE**: Siempre configura listas `allowFrom` para uso en producción.

```json
{
  "channels": {
    "telegram": {
      "enabled": true,
      "token": "TU_TOKEN_DE_BOT",
      "allowFrom": ["123456789", "987654321"]
    },
    "whatsapp": {
      "enabled": true,
      "allowFrom": ["+1234567890"]
    }
  }
}
```

**Notas de Seguridad:**
- Una lista `allowFrom` vacía **PERMITIRÁ A TODOS** los usuarios (abierto por defecto para uso personal)
- Obtén tu ID de usuario de Telegram de `@userinfobot`
- Usa números de teléfono completos con código de país para WhatsApp
- Revisa los logs de acceso regularmente para intentos de acceso no autorizados

### 3. Ejecución de Comandos Shell

La herramienta `exec` puede ejecutar comandos shell. Aunque patrones de comandos peligrosos son bloqueados, deberías:

- ✅ Revisar todo uso de herramientas en los logs del agente
- ✅ Entender qué comandos está ejecutando el agente
- ✅ Usar una cuenta de usuario dedicada con privilegios limitados
- ✅ Nunca ejecutar nanobot como root
- ❌ No deshabilitar las verificaciones de seguridad
- ❌ No ejecutar en sistemas con datos sensibles sin revisión cuidadosa

**Patrones bloqueados:**
- `rm -rf /` - Borrado del sistema de archivos raíz
- Bombas fork
- Formateo de sistema de archivos (`mkfs.*`)
- Escrituras directas a disco (raw disk writes)
- Otras operaciones destructivas

### 4. Acceso al Sistema de Archivos

Las operaciones de archivos tienen protección contra recorrido de rutas, pero:

- ✅ Ejecuta nanobot con una cuenta de usuario dedicada
- ✅ Usa permisos del sistema de archivos para proteger directorios sensibles
- ✅ Audita regularmente operaciones de archivos en logs
- ❌ No des acceso irrestricto a archivos sensibles

### 5. Seguridad de Red

**Llamadas API:**
- Todas las llamadas API externas usan HTTPS por defecto
- Los tiempos de espera (timeouts) están configurados para prevenir peticiones colgadas
- Considera usar un firewall para restringir conexiones salientes si es necesario

**Puente de WhatsApp:**
- El puente corre en `localhost:3001` por defecto
- Si se expone a la red, usa autenticación apropiada y TLS
- Mantén los datos de autenticación en `~/.nanobot/whatsapp-auth` seguros (modo 0700)

### 6. Seguridad de Dependencias

**Crítico**: ¡Mantén las dependencias actualizadas!

```bash
# Verificar dependencias vulnerables
pip install pip-audit
pip-audit

# Actualizar a las últimas versiones seguras
pip install --upgrade nanobot-ai
```

Para dependencias de Node.js (puente de WhatsApp):
```bash
cd bridge
npm audit
npm audit fix
```

**Notas Importantes:**
- Mantén `litellm` actualizado a la última versión para arreglos de seguridad
- Hemos actualizado `ws` a `>=8.17.1` para arreglar vulnerabilidad DoS
- Ejecuta `pip-audit` o `npm audit` regularmente
- Suscríbete a avisos de seguridad para nanobot y sus dependencias

### 7. Despliegue en Producción

Para uso en producción:

1. **Aísla el Entorno**
   ```bash
   # Ejecutar en un contenedor o VM
   docker run --rm -it python:3.11
   pip install nanobot-ai
   ```

2. **Usa un Usuario Dedicado**
   ```bash
   sudo useradd -m -s /bin/bash nanobot
   sudo -u nanobot nanobot gateway
   ```

3. **Establece Permisos Apropiados**
   ```bash
   chmod 700 ~/.nanobot
   chmod 600 ~/.nanobot/config.json
   chmod 700 ~/.nanobot/whatsapp-auth
   ```

4. **Habilita Logging**
   ```bash
   # Configurar monitoreo de logs
   tail -f ~/.nanobot/logs/nanobot.log
   ```

5. **Usa Límites de Tasa (Rate Limiting)**
   - Configura límites de tasa en tus proveedores de API
   - Monitorea uso para anomalías
   - Establece límites de gasto en APIs de LLM

6. **Actualizaciones Regulares**
   ```bash
   # Buscar actualizaciones semanalmente
   pip install --upgrade nanobot-ai
   ```

### 8. Desarrollo vs Producción

**Desarrollo:**
- Usa claves API separadas
- Prueba con datos no sensibles
- Habilita logging detallado (verbose)
- Usa un bot de Telegram de prueba

**Producción:**
- Usa claves API dedicadas con límites de gasto
- Restringe acceso al sistema de archivos
- Habilita logging de auditoría
- Revisiones de seguridad regulares
- Monitorea actividad inusual

### 9. Privacidad de Datos

- **Los logs pueden contener información sensible** - asegura los archivos de log apropiadamente
- **Los proveedores de LLM ven tus prompts** - revisa sus políticas de privacidad
- **El historial de chat se almacena localmente** - protege el directorio `~/.nanobot`
- **Las claves API están en texto plano** - usa keyring del SO para producción

### 10. Respuesta a Incidentes

Si sospechas una brecha de seguridad:

1. **Inmediatamente revoca claves API comprometidas**
2. **Revisa logs para acceso no autorizado**
   ```bash
   grep "Access denied" ~/.nanobot/logs/nanobot.log
   ```
3. **Verifica modificaciones de archivos inesperadas**
4. **Rota todas las credenciales**
5. **Actualiza a la última versión**
6. **Reporta el incidente** a los mantenedores

## Características de Seguridad

### Controles de Seguridad Integrados

✅ **Validación de Entrada**
- Protección contra recorrido de rutas en operaciones de archivos
- Detección de patrones de comandos peligrosos
- Límites de longitud de entrada en peticiones HTTP

✅ **Autenticación**
- Control de acceso basado en lista de permitidos (allow-list)
- Logging de intentos de autenticación fallidos
- Abierto por defecto (configura allowFrom para uso en producción)

✅ **Protección de Recursos**
- Tiempos de espera de ejecución de comandos (60s por defecto)
- Truncamiento de salida (límite de 10KB)
- Tiempos de espera de peticiones HTTP (10-30s)

✅ **Comunicación Segura**
- HTTPS para todas las llamadas API externas
- TLS para API de Telegram
- Seguridad WebSocket para puente de WhatsApp

## Limitaciones Conocidas

⚠️ **Limitaciones de Seguridad Actuales:**

1. **Sin Límite de Tasa** - Los usuarios pueden enviar mensajes ilimitados (añade el tuyo si es necesario)
2. **Configuración en Texto Plano** - Claves API almacenadas en texto plano (usa keyring para producción)
3. **Sin Gestión de Sesión** - Sin expiración automática de sesión
4. **Filtrado de Comandos Limitado** - Solo bloquea patrones peligrosos obvios
5. **Sin Rastro de Auditoría** - Logging de eventos de seguridad limitado (mejora según sea necesario)

## Lista de Verificación de Seguridad

Antes de desplegar nanobot:

- [ ] Claves API almacenadas de forma segura (no en código)
- [ ] Permisos de archivo de configuración establecidos a 0600
- [ ] Listas `allowFrom` configuradas para todos los canales
- [ ] Ejecutando como usuario no-root
- [ ] Permisos del sistema de archivos restringidos apropiadamente
- [ ] Dependencias actualizadas a las últimas versiones seguras
- [ ] Logs monitoreados para eventos de seguridad
- [ ] Límites de tasa configurados en proveedores de API
- [ ] Plan de respaldo y recuperación ante desastres en su lugar
- [ ] Revisión de seguridad de habilidades/herramientas personalizadas

## Actualizaciones

**Última Actualización**: 2026-02-03

Para las últimas actualizaciones de seguridad y anuncios, revisa:
- Avisos de Seguridad de GitHub: https://github.com/HKUDS/nanobot/security/advisories
- Notas de Lanzamiento: https://github.com/HKUDS/nanobot/releases

## Licencia

Ver archivo LICENSE para detalles.
