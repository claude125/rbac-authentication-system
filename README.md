<div align="center">

![header](https://capsule-render.vercel.app/api?type=waving&color=0:030712,50:0a1628,100:ffb700&height=200&section=header&text=RBAC%20Authentication%20System&fontSize=42&fontColor=ffffff&fontAlignY=38&desc=Role-Based%20Access%20Control%20for%20Secure%20Permission%20Management&descSize=15&descAlignY=58&animation=fadeIn)

[![Typing SVG](https://readme-typing-svg.demolab.com?font=Fira+Code&weight=500&size=14&pause=1500&color=FFB700&center=true&vCenter=true&width=750&height=40&lines=🔐+Role-Based+Access+Control+(RBAC)+in+Python;👤+Admin+%2F+Manager+%2F+User+Permission+Layers;🛡️+Secure+Authentication+%26+Access+Management;⚡+CLI+%2B+API-Ready+Architecture;🔗+JWT+%2F+OAuth+Integration+Roadmap)](https://git.io/typing-svg)

<br/>

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Security](https://img.shields.io/badge/Security-Authentication-ffb700?style=for-the-badge&logo=hackthebox&logoColor=black)
![RBAC](https://img.shields.io/badge/RBAC-Access_Control-0077b6?style=for-the-badge&logoColor=white)
![JWT](https://img.shields.io/badge/JWT-Ready-000000?style=for-the-badge&logo=jsonwebtokens&logoColor=white)
![OAuth](https://img.shields.io/badge/OAuth-Roadmap-EB5424?style=for-the-badge&logo=auth0&logoColor=white)
![CLI](https://img.shields.io/badge/CLI-Tool-0d1117?style=for-the-badge&logo=windowsterminal&logoColor=white)

</div>

---

## 🔐 What Is This?

In any multi-user system, **not everyone should have access to everything**. Giving every user full permissions is a security disaster waiting to happen.

The **RBAC Authentication System** solves this with a clean, extensible Role-Based Access Control implementation in Python. Assign roles to users, attach permissions to roles, and let the system enforce boundaries automatically — whether you're building a CLI tool, a REST API, or an enterprise application.

---

## ✨ Features

| Feature | Description |
|---|---|
| 👤 **User Authentication** | Secure login with credential validation |
| 🎭 **Role Assignment** | Assign one or more roles to each user |
| 🔑 **Permission Control** | Each role carries a defined permission set |
| 🚫 **Access Enforcement** | Requests checked against role permissions before execution |
| 📋 **Audit Trail** | Logs access attempts — granted and denied |
| ⚡ **Lightweight CLI** | Run standalone or integrate into larger systems |

---

## 🏗️ How RBAC Works

```
┌──────────────────────────────────────────────────────────────┐
│                    RBAC ACCESS MODEL                         │
├──────────────┬───────────────────┬───────────────────────────┤
│    USERS     │      ROLES        │       PERMISSIONS         │
│              │                   │                           │
│  👤 alice    │──→ 👑 Admin      │──→ create / read /        │
│              │                   │    update / delete        │
│  👤 bob      │──→ 📋 Manager    │──→ read / write           │
│              │                   │    create / update        │
│  👤 carol    │──→ 👁️  Viewer     │──→ read only              │
│              │                   │                           │
│  👤 dave     │──→ 📋 Manager    │──→ read / write           │
│              │──→ 👁️  Viewer     │    create / update        │
└──────────────┴───────────────────┴───────────────────────────┘
```

**Access Check Flow:**
```
User Login → Credential Verification
                    ↓
            Role Lookup for User
                    ↓
         Permission Check for Action
                    ↓
        ┌───────────┴───────────┐
    ✅ GRANTED              ❌ DENIED
    Execute Action          Log + Reject
```

---

## 👥 Role Definitions

| Role | Permissions | Use Case |
|---|---|---|
| 👑 **Admin** | `create` `read` `update` `delete` `manage_users` | Full system control |
| 📋 **Manager** | `create` `read` `update` | Team-level operations |
| 👁️ **Viewer** | `read` | Read-only access |
| 🔧 **Operator** | `read` `update` | Operational tasks, no delete |

> Roles are fully configurable — add, modify, or extend without changing core logic.

---

## 📊 Example Output

```
╔═══════════════════════════════════════════════════════════════╗
║            RBAC AUTHENTICATION SYSTEM  v1.0                  ║
╠═══════════════════════════════════════════════════════════════╣
║                                                               ║
║  LOGIN                                                        ║
║  ──────────────────────────────────────────────────────────  ║
║  Username  : alice                                            ║
║  Password  : ••••••••                                         ║
║  Status    : ✅ Authenticated                                 ║
║  Role      : 👑 Admin                                         ║
║  Permissions: create | read | update | delete | manage_users  ║
║                                                               ║
╠═══════════════════════════════════════════════════════════════╣
║                                                               ║
║  ACCESS LOG                                                   ║
║  ──────────────────────────────────────────────────────────  ║
║  [✅ GRANTED]  alice    → delete_user   (Admin)               ║
║  [✅ GRANTED]  bob      → create_report (Manager)             ║
║  [❌ DENIED ]  carol    → delete_file   (Viewer — no perms)   ║
║  [❌ DENIED ]  unknown  → read_data     (Auth failed)         ║
║  [✅ GRANTED]  dave     → update_record (Manager)             ║
║                                                               ║
╠═══════════════════════════════════════════════════════════════╣
║  Total requests : 5   Granted : 3   Denied : 2               ║
╚═══════════════════════════════════════════════════════════════╝
```

---

## 🚀 Quick Start

```bash
# 1. Clone the repository
git clone https://github.com/claude125/rbac-authentication-system.git
cd rbac-authentication-system

# 2. Run the system
python rbac_system.py
```

---

## ⚙️ Configuration

```python
# Define roles and permissions in rbac_system.py

ROLES = {
    "Admin"    : ["create", "read", "update", "delete", "manage_users"],
    "Manager"  : ["create", "read", "update"],
    "Viewer"   : ["read"],
    "Operator" : ["read", "update"],
}

USERS = {
    "alice" : {"password": "hashed_pw_here", "roles": ["Admin"]},
    "bob"   : {"password": "hashed_pw_here", "roles": ["Manager"]},
    "carol" : {"password": "hashed_pw_here", "roles": ["Viewer"]},
    "dave"  : {"password": "hashed_pw_here", "roles": ["Manager", "Viewer"]},
}
```

---

## 🧰 Tech Stack

```
Python 3.x      — Core language
hashlib         — Password hashing
json / dict     — Role & permission store
argparse        — CLI interface
logging         — Access audit trail
```

---

## 📁 Project Structure

```
rbac-authentication-system/
│
├── 📄 rbac_system.py      # Core RBAC engine
├── 📄 requirements.txt    # Python dependencies
└── 📄 README.md
```

---

## 🌍 Who Is This For?

`🏢 Enterprise Apps` &nbsp; `🔐 Security Engineers` &nbsp; `🌐 API Developers` &nbsp; `🎓 Auth & IAM Learners` &nbsp; `☁️ Cloud IAM Teams`

---

## 🚀 Roadmap

```python
roadmap = [
    "🗄️  Database integration (PostgreSQL / SQLite)",
    "🌐 REST API authentication support",
    "🔑 JWT token-based stateless auth",
    "🔗 OAuth 2.0 / OpenID Connect integration",
    "🖥️  Web-based user & role management UI",
    "📊 Admin dashboard with access analytics",
    "🏢 LDAP / Active Directory integration",
]
```

---

## 👤 Author

<div align="center">

**Claude Dusengimana**
*Senior Network & Security Engineer | IoT Researcher*
📍 Kigali, Rwanda

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/dusengimana-claude)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-161b22?style=for-the-badge&logo=github&logoColor=white)](https://github.com/claude125)
[![Gmail](https://img.shields.io/badge/Email-Contact-EA4335?style=for-the-badge&logo=gmail&logoColor=white)](mailto:dusenge125@gmail.com)

</div>

---

<div align="center">

![footer](https://capsule-render.vercel.app/api?type=waving&color=0:ffb700,50:0a1628,100:030712&height=100&section=footer&text=Right+access.+Right+people.+Right+time.&fontSize=14&fontColor=ffffff&fontAlignY=65&animation=fadeIn)

*⭐ Star this repo if it helped you think about access control differently.*

</div>
