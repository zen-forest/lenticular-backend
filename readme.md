# Lenticular Backend
A robust and reusable REST API template designed to support 10,000 MAUs seamlessly. Unlocks prototyping velocity while maintaining top-tier performance, security, and scalability.

- [ ] Email is case sensitive 
- [ ] how do I de-dupe URLs / add attribution? 

---


## Architecture
* Django/Django REST Framework
* Postgresql
	* The OG - ACID compliance
	* Full-text search (great for search, typeahead, etc) 
	* Optimizations like indexing
	* Scalability
	* Add’ on’s like PostGIS (geographic database)
* JWT tokens for authentication
* Future proof user model
* If needed: Redis (caching, Celery jobs, etc)
* Render for hosting and deployments
* Cloudflare (Security features/CDN)
* Only maintained 3rd party libraries are used

**Rough costs**
For 1,000 users, ~$69 per month 
For 10,000 users - $251 per month



### 2. Tooling
| Category             | Feature                                     | Sub-features                                    |
|----------------------|---------------------------------------------|------------------------------------------------|
| **Render** | Database hosting                           |                                                |
|                      | App                                         |                                                |
|                      | GitHub action deployments                  |                                                |
|                      | Custom Domain                               |                                                |
|                      | ENV                                         |                                                |
|                      | Health checks                               |                                                |
|                      | Background workers                          | Email sending, Batch sending                   |
|                      | Service monitoring                          |                                                |
| **Cloudflare**       | SSL for encryption                          |                                                |
|                      | DNS                                         |                                                |
|                      | DDoS protection                             |                                                |
|                      | Caching                                     |                                                |
|                      | Rate limiting                               |                                                |
|                      | Firewall rules                              | Malicious IP blocking                          |
|                      | Analytics                                   |                                                |
| **Sentry**           | Error tracking                              | Exceptions, crashes, errors, Stack traces      |
|                      | Performance monitoring                      | Response times, Query performance, Slow endpoints |
|                      | Alerts                                      | Errors, Downtime                               |
|                      | Environmental context                       |                                                |


**Further deployment tooling**
* Docker
* Staging vs. production environments


**Add as-needed**
* Django Debug Toolbar
* Social auth: django-allauth, dj-rest-auth social-auth-app-django
* Serve static files with Whitenoise
* Automated API documentation
* Sendgrid for email
* Twilio for SMS
* Stripe for Payments
* Slack for Webhooks, notifs, etc. 


## 4. Django security hardening 

## Authentication
- **Password Hashing**
  - Uses PBKDF2 by default.
  - Recommended: Switch to bcrypt or Argon2 for stronger security.
- **JWT Security**
  - Use **short-lived tokens** (e.g., 15 minutes for access tokens).
  - Use **refresh tokens** for long-term access.
  - Avoid storing JWTs in `localStorage`. Use `HttpOnly` cookies for client-side storage.
  - Implement token blacklisting for logout and password resets (e.g., using `django-rest-framework-simplejwt`).
- **Role-Based Access Control (Optional)**
  - Add roles like `admin`, `user`, or `moderator` to the `User` model.
  - Use custom DRF permissions for role-based access control.


## Request validation and rate limiting
- **Rate Limiting**
  - Use DRF’s `UserRateThrottle` and `AnonRateThrottle` to limit requests per user or IP.
  - Apply stricter limits to sensitive endpoints like login and password reset.
- **Input Validation**
  - Use DRF serializers to validate and sanitize incoming data.


## Built-in protections
- **CSRF Protection**
  - Enabled by default for browser-facing views.
  - Not required for JWT-based APIs.
- **SQL Injection Prevention**
  - Django ORM parameterizes queries to prevent injection attacks.
- **XSS Protection**
  - Templates auto-escape variables by default (relevant if your API serves templates).
- **Clickjacking Protection**
  - Use `XFrameOptionsMiddleware` (enabled by default) to add the `X-Frame-Options` header.


## Secure cookies and headers
- **Secure Cookies**
  - Set `HttpOnly`, `Secure`, and `SameSite` attributes for cookies if JWT is stored client-side.
- **HTTP Security Headers**
  - Enable `SECURE_HSTS_SECONDS` to enforce HTTP Strict Transport Security (HSTS).
  - Set `SECURE_CONTENT_TYPE_NOSNIFF = True` to prevent MIME type sniffing.


## Production settings
- **Debugging**
  - Set `DEBUG = False` in production to avoid exposing sensitive information.
- **Allowed Hosts**
  - Define valid domains in the `ALLOWED_HOSTS` setting.
- **Enforce HTTPS**
  - Use `SECURE_SSL_REDIRECT = True` to redirect HTTP traffic to HTTPS.
  - Configure `SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')` when behind a proxy like Render.


## Monitoring and logging
- **Log Security Events**
  - Record failed logins, token invalidations, and suspicious requests.
- **Error Tracking**
  - Use tools like Sentry to monitor application errors and security issues.


## CORS policies
- Use `django-cors-headers` to allow only trusted origins for API access.

---

