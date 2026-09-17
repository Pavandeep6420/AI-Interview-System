import random


QUESTIONS = {

    # =========================================================
    # JAVA DEVELOPER
    # =========================================================

    "Java Developer": {

        "Easy": [
            ("What is Java and what are its main features?",
             ["java", "platform independent", "object oriented"]),

            ("What is the difference between JDK, JRE and JVM?",
             ["jdk", "jre", "jvm"]),

            ("What is a class and object in Java?",
             ["class", "object", "instance"]),

            ("What are the primitive data types in Java?",
             ["primitive", "int", "boolean", "char"]),

            ("What is inheritance in Java?",
             ["inheritance", "extends", "parent"]),

            ("What is encapsulation?",
             ["encapsulation", "private", "getter", "setter"]),

            ("What is polymorphism in Java?",
             ["polymorphism", "overloading", "overriding"]),

            ("What is the difference between == and equals()?",
             ["equals", "comparison", "reference"]),

            ("What is a constructor?",
             ["constructor", "class", "object"]),

            ("What is an interface in Java?",
             ["interface", "implements", "abstract"]),

            ("What is exception handling?",
             ["exception", "try", "catch", "finally"]),

            ("What is the difference between Array and ArrayList?",
             ["array", "arraylist", "dynamic"])
        ],

        "Medium": [
            ("Explain method overloading and method overriding.",
             ["overloading", "overriding", "method"]),

            ("Explain abstract classes and interfaces.",
             ["abstract", "interface", "implements"]),

            ("What is the Java Collections Framework?",
             ["collections", "list", "set", "map"]),

            ("Explain HashMap and how it works.",
             ["hashmap", "hashing", "key", "value"]),

            ("What is the difference between ArrayList and LinkedList?",
             ["arraylist", "linkedlist", "insertion"]),

            ("Explain HashSet and TreeSet.",
             ["hashset", "treeset", "duplicate"]),

            ("What is multithreading in Java?",
             ["thread", "multithreading", "concurrency"]),

            ("What is synchronization?",
             ["synchronization", "thread", "lock"]),

            ("Explain garbage collection in Java.",
             ["garbage", "memory", "heap"]),

            ("What is the difference between checked and unchecked exceptions?",
             ["checked", "unchecked", "exception"]),

            ("What are access modifiers in Java?",
             ["public", "private", "protected", "default"]),

            ("Explain static keyword in Java.",
             ["static", "class", "method", "variable"])
        ],

        "Hard": [
            ("Explain JVM memory areas.",
             ["jvm", "heap", "stack", "memory"]),

            ("How does garbage collection work internally?",
             ["garbage", "collector", "heap", "memory"]),

            ("Explain Java thread lifecycle.",
             ["thread", "lifecycle", "new", "running"]),

            ("What is ExecutorService?",
             ["executorservice", "threadpool", "concurrency"]),

            ("Explain ConcurrentHashMap.",
             ["concurrenthashmap", "concurrency", "thread"]),

            ("What is the Java Memory Model?",
             ["memory", "visibility", "thread", "jmm"]),

            ("Explain deadlock and how to prevent it.",
             ["deadlock", "lock", "thread", "synchronization"]),

            ("What are volatile variables?",
             ["volatile", "visibility", "thread"]),

            ("Explain functional interfaces and lambda expressions.",
             ["functional", "interface", "lambda"]),

            ("What are Java Streams?",
             ["stream", "filter", "map", "reduce"]),

            ("Explain CompletableFuture.",
             ["completablefuture", "asynchronous", "future"]),

            ("How can Java applications be optimized for performance?",
             ["performance", "memory", "optimization", "profiling"])
        ]
    },


    # =========================================================
    # PYTHON DEVELOPER
    # =========================================================

    "Python Developer": {

        "Easy": [
            ("What is Python and why is it popular?",
             ["python", "interpreted", "readable"]),

            ("What are Python variables?",
             ["variable", "python", "dynamic"]),

            ("What are Python data types?",
             ["int", "string", "list", "tuple"]),

            ("What is a list in Python?",
             ["list", "mutable", "sequence"]),

            ("What is a tuple?",
             ["tuple", "immutable", "sequence"]),

            ("What is a dictionary?",
             ["dictionary", "key", "value"]),

            ("What is a set in Python?",
             ["set", "unique", "unordered"]),

            ("What is indentation in Python?",
             ["indentation", "block", "python"]),

            ("What is a function?",
             ["function", "def", "return"]),

            ("What is a module?",
             ["module", "import", "python"]),

            ("What is exception handling?",
             ["exception", "try", "except"]),

            ("What is a Python virtual environment?",
             ["virtual", "environment", "venv"])
        ],

        "Medium": [
            ("Explain list comprehension.",
             ["list", "comprehension", "loop"]),

            ("Explain dictionary comprehension.",
             ["dictionary", "comprehension", "key"]),

            ("What are lambda functions?",
             ["lambda", "function", "anonymous"]),

            ("Explain *args and **kwargs.",
             ["args", "kwargs", "function"]),

            ("What are decorators?",
             ["decorator", "function", "wrapper"]),

            ("Explain generators.",
             ["generator", "yield", "iterator"]),

            ("What is the difference between shallow and deep copy?",
             ["shallow", "deep", "copy"]),

            ("What is object-oriented programming in Python?",
             ["class", "object", "inheritance"]),

            ("Explain inheritance in Python.",
             ["inheritance", "class", "parent"]),

            ("What is the difference between list and tuple?",
             ["list", "tuple", "mutable"]),

            ("Explain Python exception handling.",
             ["try", "except", "finally"]),

            ("What is pip?",
             ["pip", "package", "install"])
        ],

        "Hard": [
            ("Explain Python memory management.",
             ["memory", "garbage", "reference"]),

            ("What is the Global Interpreter Lock?",
             ["gil", "thread", "python"]),

            ("Explain multiprocessing versus multithreading.",
             ["multiprocessing", "multithreading", "process"]),

            ("What are asynchronous functions in Python?",
             ["async", "await", "asynchronous"]),

            ("Explain Python iterators and iterables.",
             ["iterator", "iterable", "iter"]),

            ("How do Python decorators work internally?",
             ["decorator", "wrapper", "function"]),

            ("Explain context managers.",
             ["context", "with", "manager"]),

            ("What are metaclasses?",
             ["metaclass", "class", "type"]),

            ("How can Python code be optimized?",
             ["optimization", "performance", "profiling"]),

            ("Explain garbage collection in Python.",
             ["garbage", "reference", "collector"]),

            ("What is monkey patching?",
             ["monkey", "patching", "runtime"]),

            ("How would you design a scalable Python backend?",
             ["python", "backend", "scalable", "architecture"])
        ]
    },


    # =========================================================
    # FRONTEND DEVELOPER
    # =========================================================

    "Frontend Developer": {

        "Easy": [
            ("What is HTML?",
             ["html", "markup", "structure"]),

            ("What is CSS?",
             ["css", "style", "design"]),

            ("What is JavaScript?",
             ["javascript", "language", "browser"]),

            ("What are HTML semantic elements?",
             ["semantic", "html", "header", "section"]),

            ("What is the CSS box model?",
             ["box", "model", "margin", "padding"]),

            ("What is responsive web design?",
             ["responsive", "mobile", "css"]),

            ("What is DOM?",
             ["dom", "document", "object"]),

            ("What are CSS selectors?",
             ["selector", "css", "class", "id"]),

            ("What is an HTML form?",
             ["form", "input", "html"]),

            ("What is the difference between id and class?",
             ["id", "class", "selector"]),

            ("What is a hyperlink?",
             ["link", "anchor", "href"]),

            ("What is viewport?",
             ["viewport", "responsive", "mobile"])
        ],

        "Medium": [
            ("Explain CSS Flexbox.",
             ["flexbox", "flex", "layout"]),

            ("Explain CSS Grid.",
             ["grid", "layout", "css"]),

            ("What is event bubbling?",
             ["event", "bubbling", "dom"]),

            ("What is event delegation?",
             ["event", "delegation", "dom"]),

            ("Explain JavaScript promises.",
             ["promise", "async", "javascript"]),

            ("What is async and await?",
             ["async", "await", "promise"]),

            ("Explain closures in JavaScript.",
             ["closure", "function", "scope"]),

            ("What is localStorage?",
             ["localstorage", "browser", "storage"]),

            ("What is sessionStorage?",
             ["sessionstorage", "browser", "storage"]),

            ("What is CORS?",
             ["cors", "browser", "origin"]),

            ("How do you optimize frontend performance?",
             ["performance", "optimization", "browser"]),

            ("What is lazy loading?",
             ["lazy", "loading", "performance"])
        ],

        "Hard": [
            ("Explain browser rendering pipeline.",
             ["browser", "rendering", "dom", "css"]),

            ("What is critical rendering path?",
             ["rendering", "css", "javascript", "performance"]),

            ("Explain JavaScript event loop.",
             ["event", "loop", "callback", "javascript"]),

            ("What are microtasks and macrotasks?",
             ["microtask", "macrotask", "event"]),

            ("How does browser caching work?",
             ["cache", "browser", "http"]),

            ("Explain web accessibility.",
             ["accessibility", "aria", "html"]),

            ("How do you prevent XSS attacks?",
             ["xss", "security", "sanitization"]),

            ("Explain code splitting.",
             ["code", "splitting", "bundle", "performance"]),

            ("How would you design a scalable frontend?",
             ["frontend", "architecture", "scalable"]),

            ("Explain service workers.",
             ["service", "worker", "cache", "pwa"]),

            ("What is a Progressive Web App?",
             ["pwa", "service", "worker"]),

            ("How would you debug a slow web application?",
             ["debug", "performance", "profiling", "browser"])
        ]
    },


    # =========================================================
    # BACKEND DEVELOPER
    # =========================================================

    "Backend Developer": {

        "Easy": [
            ("What is backend development?",
             ["backend", "server", "database"]),

            ("What is an API?",
             ["api", "request", "response"]),

            ("What is REST API?",
             ["rest", "api", "http"]),

            ("What is HTTP?",
             ["http", "request", "response"]),

            ("What is a server?",
             ["server", "request", "client"]),

            ("What is a database?",
             ["database", "data", "storage"]),

            ("What is JSON?",
             ["json", "data", "api"]),

            ("What is authentication?",
             ["authentication", "login", "identity"]),

            ("What is authorization?",
             ["authorization", "permission", "access"]),

            ("What is CRUD?",
             ["crud", "create", "read", "update", "delete"]),

            ("What is HTTP status code?",
             ["http", "status", "response"]),

            ("What is middleware?",
             ["middleware", "request", "response"])
        ],

        "Medium": [
            ("Explain REST API principles.",
             ["rest", "stateless", "resource"]),

            ("What is JWT authentication?",
             ["jwt", "token", "authentication"]),

            ("Explain session-based authentication.",
             ["session", "authentication", "cookie"]),

            ("What is API rate limiting?",
             ["rate", "limit", "api"]),

            ("What is database indexing?",
             ["index", "database", "query"]),

            ("Explain database transactions.",
             ["transaction", "commit", "rollback"]),

            ("What is caching?",
             ["cache", "performance", "database"]),

            ("What is load balancing?",
             ["load", "balancer", "server"]),

            ("Explain pagination in APIs.",
             ["pagination", "api", "page"]),

            ("What is input validation?",
             ["validation", "input", "security"]),

            ("What is API versioning?",
             ["api", "version", "endpoint"]),

            ("How do you handle backend errors?",
             ["error", "exception", "logging"])
        ],

        "Hard": [
            ("How would you design a scalable backend system?",
             ["scalable", "backend", "architecture"]),

            ("Explain horizontal and vertical scaling.",
             ["horizontal", "vertical", "scaling"]),

            ("Explain distributed caching.",
             ["distributed", "cache", "redis"]),

            ("What is database sharding?",
             ["sharding", "database", "distributed"]),

            ("What is eventual consistency?",
             ["eventual", "consistency", "distributed"]),

            ("Explain message queues.",
             ["message", "queue", "async"]),

            ("What is microservices architecture?",
             ["microservices", "service", "architecture"]),

            ("Explain circuit breaker pattern.",
             ["circuit", "breaker", "microservice"]),

            ("How do you secure backend APIs?",
             ["security", "api", "authentication"]),

            ("How would you handle millions of requests?",
             ["scaling", "load", "cache", "server"]),

            ("Explain database replication.",
             ["replication", "database", "primary", "replica"]),

            ("How do you monitor production backend systems?",
             ["monitoring", "logging", "metrics"])
        ]
    },


    # =========================================================
    # FULL STACK DEVELOPER
    # =========================================================

    "Full Stack Developer": {

        "Easy": [
            ("What is full stack development?",
             ["frontend", "backend", "database"]),

            ("What is the difference between frontend and backend?",
             ["frontend", "backend", "server"]),

            ("What is HTML?",
             ["html", "markup"]),

            ("What is CSS?",
             ["css", "style"]),

            ("What is JavaScript?",
             ["javascript", "browser"]),

            ("What is an API?",
             ["api", "request", "response"]),

            ("What is a database?",
             ["database", "storage"]),

            ("What is SQL?",
             ["sql", "database", "query"]),

            ("What is Git?",
             ["git", "version", "control"]),

            ("What is authentication?",
             ["authentication", "login"]),

            ("What is CRUD?",
             ["crud", "create", "read", "update", "delete"]),

            ("What is deployment?",
             ["deployment", "server", "application"])
        ],

        "Medium": [
            ("Explain frontend-backend communication.",
             ["frontend", "backend", "api"]),

            ("How does REST API work?",
             ["rest", "api", "http"]),

            ("Explain JWT authentication.",
             ["jwt", "token", "authentication"]),

            ("How do you connect a backend to a database?",
             ["backend", "database", "connection"]),

            ("What is MVC architecture?",
             ["mvc", "model", "view", "controller"]),

            ("What is responsive design?",
             ["responsive", "css", "mobile"]),

            ("Explain React components.",
             ["react", "component", "props"]),

            ("What is middleware?",
             ["middleware", "request", "response"]),

            ("How do you handle API errors?",
             ["api", "error", "exception"]),

            ("What is CORS?",
             ["cors", "origin", "browser"]),

            ("What is environment configuration?",
             ["environment", "configuration", "variable"]),

            ("How do you deploy a full stack application?",
             ["deploy", "frontend", "backend", "server"])
        ],

        "Hard": [
            ("Design a scalable full stack application.",
             ["scalable", "frontend", "backend", "database"]),

            ("Explain microservices architecture.",
             ["microservices", "service", "architecture"]),

            ("How would you optimize full stack performance?",
             ["performance", "frontend", "backend", "database"]),

            ("Explain database indexing and optimization.",
             ["database", "index", "query", "optimization"]),

            ("How would you secure a full stack application?",
             ["security", "authentication", "authorization"]),

            ("Explain caching strategies.",
             ["cache", "redis", "performance"]),

            ("What is CI/CD?",
             ["ci", "cd", "deployment"]),

            ("How would you design authentication for a large application?",
             ["authentication", "jwt", "session", "security"]),

            ("How do you handle high traffic?",
             ["scaling", "load", "cache"]),

            ("Explain Docker in full stack development.",
             ["docker", "container", "deployment"]),

            ("How do you monitor a production application?",
             ["monitoring", "logging", "metrics"]),

            ("Explain cloud deployment architecture.",
             ["cloud", "server", "deployment"])
        ]
    },


    # =========================================================
    # REACT DEVELOPER
    # =========================================================

    "React Developer": {

        "Easy": [
            ("What is React?",
             ["react", "component", "javascript"]),

            ("What is a React component?",
             ["component", "react", "jsx"]),

            ("What is JSX?",
             ["jsx", "javascript", "html"]),

            ("What are props?",
             ["props", "component", "data"]),

            ("What is state?",
             ["state", "component", "react"]),

            ("What is useState?",
             ["usestate", "state", "hook"]),

            ("What is useEffect?",
             ["useeffect", "hook", "effect"]),

            ("What are React Hooks?",
             ["hooks", "react", "state"]),

            ("What is conditional rendering?",
             ["conditional", "rendering", "react"]),

            ("How do you render lists in React?",
             ["list", "map", "key"]),

            ("Why are keys used in React?",
             ["key", "list", "react"]),

            ("What is React Router?",
             ["router", "react", "route"])
        ],

        "Medium": [
            ("Explain component lifecycle.",
             ["lifecycle", "component", "effect"]),

            ("What is prop drilling?",
             ["prop", "drilling", "component"]),

            ("What is Context API?",
             ["context", "api", "react"]),

            ("Explain useMemo.",
             ["usememo", "performance", "hook"]),

            ("Explain useCallback.",
             ["usecallback", "function", "performance"]),

            ("What is React.memo?",
             ["react", "memo", "performance"]),

            ("Explain controlled components.",
             ["controlled", "form", "state"]),

            ("What are uncontrolled components?",
             ["uncontrolled", "form", "ref"]),

            ("How do you call APIs in React?",
             ["api", "fetch", "axios"]),

            ("How do you manage forms in React?",
             ["form", "state", "input"]),

            ("What is lifting state up?",
             ["state", "lifting", "component"]),

            ("How do you optimize React applications?",
             ["optimization", "performance", "react"])
        ],

        "Hard": [
            ("Explain React reconciliation.",
             ["reconciliation", "virtual", "dom"]),

            ("How does the Virtual DOM work?",
             ["virtual", "dom", "render"]),

            ("Explain React Fiber.",
             ["fiber", "react", "rendering"]),

            ("How does concurrent rendering work?",
             ["concurrent", "rendering", "react"]),

            ("How would you optimize a large React application?",
             ["optimization", "performance", "bundle"]),

            ("Explain code splitting in React.",
             ["code", "splitting", "lazy"]),

            ("What is server-side rendering?",
             ["ssr", "server", "rendering"]),

            ("What is hydration?",
             ["hydration", "ssr", "react"]),

            ("How would you structure a large React project?",
             ["architecture", "component", "react"]),

            ("Explain React state management strategies.",
             ["state", "redux", "context"]),

            ("How do you prevent unnecessary React renders?",
             ["render", "memo", "performance"]),

            ("How do you secure a React application?",
             ["security", "xss", "authentication"])
        ]
    },


    # =========================================================
    # JAVASCRIPT DEVELOPER
    # =========================================================

    "JavaScript Developer": {

        "Easy": [
            ("What is JavaScript?",
             ["javascript", "language", "browser"]),

            ("What are JavaScript variables?",
             ["variable", "let", "const"]),

            ("Difference between let, var and const?",
             ["let", "var", "const"]),

            ("What are JavaScript data types?",
             ["string", "number", "boolean", "object"]),

            ("What is an array?",
             ["array", "javascript", "list"]),

            ("What is an object?",
             ["object", "property", "javascript"]),

            ("What is a function?",
             ["function", "return", "javascript"]),

            ("What is an arrow function?",
             ["arrow", "function", "javascript"]),

            ("What is DOM?",
             ["dom", "document", "browser"]),

            ("What is an event?",
             ["event", "click", "javascript"]),

            ("What is JSON?",
             ["json", "javascript", "data"]),

            ("What is NaN?",
             ["nan", "number", "javascript"])
        ],

        "Medium": [
            ("Explain closures.",
             ["closure", "scope", "function"]),

            ("Explain hoisting.",
             ["hoisting", "variable", "function"]),

            ("What is the event loop?",
             ["event", "loop", "javascript"]),

            ("Explain promises.",
             ["promise", "async", "javascript"]),

            ("What is async/await?",
             ["async", "await", "promise"]),

            ("Explain callbacks.",
             ["callback", "function", "async"]),

            ("What is destructuring?",
             ["destructuring", "array", "object"]),

            ("Explain spread and rest operators.",
             ["spread", "rest", "operator"]),

            ("What is prototype inheritance?",
             ["prototype", "inheritance", "object"]),

            ("What is the difference between map, filter and reduce?",
             ["map", "filter", "reduce"]),

            ("Explain event bubbling and capturing.",
             ["bubbling", "capturing", "event"]),

            ("What is localStorage?",
             ["localstorage", "browser", "storage"])
        ],

        "Hard": [
            ("Explain the JavaScript runtime architecture.",
             ["runtime", "engine", "event", "loop"]),

            ("Explain microtask and macrotask queues.",
             ["microtask", "macrotask", "queue"]),

            ("How does garbage collection work in JavaScript?",
             ["garbage", "memory", "collector"]),

            ("Explain prototypal inheritance internally.",
             ["prototype", "inheritance", "object"]),

            ("What is the JavaScript execution context?",
             ["execution", "context", "scope"]),

            ("Explain lexical environment.",
             ["lexical", "environment", "scope"]),

            ("What are generators?",
             ["generator", "yield", "iterator"]),

            ("What are Web Workers?",
             ["web", "worker", "thread"]),

            ("How would you optimize JavaScript performance?",
             ["performance", "optimization", "javascript"]),

            ("Explain memory leaks in JavaScript.",
             ["memory", "leak", "javascript"]),

            ("How do you secure JavaScript applications?",
             ["security", "xss", "javascript"]),

            ("Explain module systems in JavaScript.",
             ["module", "import", "export"])
        ]
    },


    # =========================================================
    # DATA ANALYST
    # =========================================================

    "Data Analyst": {

        "Easy": [
            ("What is data analysis?",
             ["data", "analysis", "insight"]),

            ("What is Excel used for in data analysis?",
             ["excel", "spreadsheet", "data"]),

            ("What is SQL?",
             ["sql", "query", "database"]),

            ("What is a database?",
             ["database", "data", "table"]),

            ("What is a row and column?",
             ["row", "column", "table"]),

            ("What is data cleaning?",
             ["cleaning", "missing", "data"]),

            ("What is a primary key?",
             ["primary", "key", "database"]),

            ("What is a filter?",
             ["filter", "data", "condition"]),

            ("What is a chart?",
             ["chart", "visualization", "data"]),

            ("What is mean?",
             ["mean", "average", "statistics"]),

            ("What is median?",
             ["median", "statistics", "data"]),

            ("What is a dashboard?",
             ["dashboard", "visualization", "data"])
        ],

        "Medium": [
            ("Explain data preprocessing.",
             ["preprocessing", "cleaning", "data"]),

            ("What is missing value treatment?",
             ["missing", "value", "imputation"]),

            ("Explain joins in SQL.",
             ["join", "sql", "table"]),

            ("What is GROUP BY in SQL?",
             ["group", "sql", "aggregate"]),

            ("What is a subquery?",
             ["subquery", "sql", "query"]),

            ("What is correlation?",
             ["correlation", "relationship", "data"]),

            ("Explain outliers.",
             ["outlier", "data", "statistics"]),

            ("What is standard deviation?",
             ["standard", "deviation", "statistics"]),

            ("What is data visualization?",
             ["visualization", "chart", "data"]),

            ("Explain Power BI.",
             ["power", "bi", "dashboard"]),

            ("What is a KPI?",
             ["kpi", "metric", "business"]),

            ("How do you validate analytical results?",
             ["validation", "analysis", "data"])
        ],

        "Hard": [
            ("How would you analyze a large dataset?",
             ["large", "dataset", "analysis"]),

            ("Explain statistical hypothesis testing.",
             ["hypothesis", "testing", "statistics"]),

            ("What is regression analysis?",
             ["regression", "statistics", "prediction"]),

            ("Explain A/B testing.",
             ["ab", "testing", "experiment"]),

            ("How do you detect data quality issues?",
             ["data", "quality", "validation"]),

            ("Explain feature engineering.",
             ["feature", "engineering", "data"]),

            ("How do you handle highly skewed data?",
             ["skewed", "data", "transformation"]),

            ("How do you optimize SQL queries?",
             ["sql", "query", "index", "optimization"]),

            ("How would you build an analytical dashboard?",
             ["dashboard", "kpi", "visualization"]),

            ("Explain ETL pipelines.",
             ["etl", "extract", "transform", "load"]),

            ("How do you communicate insights to business teams?",
             ["insight", "business", "communication"]),

            ("How would you analyze customer churn?",
             ["churn", "customer", "analysis"])
        ]
    },


    # =========================================================
    # DATA SCIENTIST
    # =========================================================

    "Data Scientist": {

        "Easy": [
            ("What is data science?",
             ["data", "science", "analysis"]),

            ("What is a dataset?",
             ["dataset", "data", "rows"]),

            ("What is a feature?",
             ["feature", "data", "variable"]),

            ("What is a target variable?",
             ["target", "variable", "prediction"]),

            ("What is supervised learning?",
             ["supervised", "label", "learning"]),

            ("What is unsupervised learning?",
             ["unsupervised", "clustering", "learning"]),

            ("What is regression?",
             ["regression", "prediction", "continuous"]),

            ("What is classification?",
             ["classification", "label", "prediction"]),

            ("What is pandas?",
             ["pandas", "python", "data"]),

            ("What is NumPy?",
             ["numpy", "array", "python"]),

            ("What is data visualization?",
             ["visualization", "data", "chart"]),

            ("What is model training?",
             ["training", "model", "data"])
        ],

        "Medium": [
            ("Explain train-test split.",
             ["train", "test", "split"]),

            ("What is cross-validation?",
             ["cross", "validation", "model"]),

            ("Explain overfitting.",
             ["overfitting", "model", "generalization"]),

            ("Explain underfitting.",
             ["underfitting", "model", "training"]),

            ("What is feature scaling?",
             ["scaling", "feature", "normalization"]),

            ("Explain precision and recall.",
             ["precision", "recall", "classification"]),

            ("What is F1 score?",
             ["f1", "precision", "recall"]),

            ("Explain confusion matrix.",
             ["confusion", "matrix", "classification"]),

            ("What is feature selection?",
             ["feature", "selection", "model"]),

            ("What is PCA?",
             ["pca", "dimensionality", "reduction"]),

            ("Explain clustering.",
             ["clustering", "unsupervised", "kmeans"]),

            ("What is ensemble learning?",
             ["ensemble", "random", "forest"])
        ],

        "Hard": [
            ("How do you handle class imbalance?",
             ["imbalance", "class", "sampling"]),

            ("Explain bias-variance tradeoff.",
             ["bias", "variance", "model"]),

            ("How do you tune machine learning models?",
             ["hyperparameter", "tuning", "model"]),

            ("Explain regularization.",
             ["regularization", "l1", "l2"]),

            ("How would you handle missing data?",
             ["missing", "imputation", "data"]),

            ("Explain gradient descent.",
             ["gradient", "descent", "optimization"]),

            ("What is feature importance?",
             ["feature", "importance", "model"]),

            ("How do you prevent data leakage?",
             ["data", "leakage", "training"]),

            ("How would you design an end-to-end ML pipeline?",
             ["pipeline", "machine", "learning"]),

            ("Explain model interpretability.",
             ["interpretability", "shap", "model"]),

            ("How do you evaluate an imbalanced classifier?",
             ["imbalanced", "precision", "recall"]),

            ("How would you deploy a machine learning model?",
             ["deployment", "model", "api"])
        ]
    },


    # =========================================================
    # MACHINE LEARNING ENGINEER
    # =========================================================

    "Machine Learning Engineer": {

        "Easy": [
            ("What is machine learning?",
             ["machine", "learning", "model"]),

            ("What is supervised learning?",
             ["supervised", "label", "training"]),

            ("What is unsupervised learning?",
             ["unsupervised", "clustering", "data"]),

            ("What is a machine learning model?",
             ["model", "training", "prediction"]),

            ("What is training data?",
             ["training", "data", "model"]),

            ("What is testing data?",
             ["testing", "data", "model"]),

            ("What is classification?",
             ["classification", "label", "prediction"]),

            ("What is regression?",
             ["regression", "prediction", "continuous"]),

            ("What is clustering?",
             ["clustering", "unsupervised", "groups"]),

            ("What is an algorithm?",
             ["algorithm", "learning", "model"]),

            ("What is accuracy?",
             ["accuracy", "classification", "metric"]),

            ("What is overfitting?",
             ["overfitting", "model", "training"])
        ],

        "Medium": [
            ("Explain linear regression.",
             ["linear", "regression", "prediction"]),

            ("Explain logistic regression.",
             ["logistic", "classification", "probability"]),

            ("Explain decision trees.",
             ["decision", "tree", "classification"]),

            ("Explain random forests.",
             ["random", "forest", "ensemble"]),

            ("What is gradient boosting?",
             ["gradient", "boosting", "ensemble"]),

            ("Explain support vector machines.",
             ["svm", "margin", "classification"]),

            ("Explain k-means clustering.",
             ["kmeans", "clustering", "centroid"]),

            ("What is cross-validation?",
             ["cross", "validation", "model"]),

            ("What is hyperparameter tuning?",
             ["hyperparameter", "tuning", "model"]),

            ("Explain regularization.",
             ["regularization", "l1", "l2"]),

            ("What is feature engineering?",
             ["feature", "engineering", "model"]),

            ("Explain model evaluation metrics.",
             ["metrics", "accuracy", "precision", "recall"])
        ],

        "Hard": [
            ("Design an end-to-end machine learning pipeline.",
             ["pipeline", "training", "deployment"]),

            ("Explain model drift.",
             ["drift", "model", "production"]),

            ("How do you monitor ML models in production?",
             ["monitoring", "model", "production"]),

            ("Explain online versus batch inference.",
             ["online", "batch", "inference"]),

            ("What is feature store?",
             ["feature", "store", "ml"]),

            ("Explain distributed machine learning.",
             ["distributed", "machine", "learning"]),

            ("How do you optimize model inference?",
             ["inference", "optimization", "model"]),

            ("Explain model quantization.",
             ["quantization", "model", "optimization"]),

            ("What is MLOps?",
             ["mlops", "machine", "deployment"]),

            ("How do you handle data drift?",
             ["data", "drift", "monitoring"]),

            ("How would you deploy an ML model as an API?",
             ["model", "api", "deployment"]),

            ("How do you ensure reproducibility in ML projects?",
             ["reproducibility", "version", "model"])
        ]
    },


    # =========================================================
    # AI ENGINEER
    # =========================================================

    "AI Engineer": {

        "Easy": [
            ("What is artificial intelligence?",
             ["artificial", "intelligence", "ai"]),

            ("What is machine learning?",
             ["machine", "learning", "ai"]),

            ("What is deep learning?",
             ["deep", "learning", "neural"]),

            ("What is a neural network?",
             ["neural", "network", "layer"]),

            ("What is an AI model?",
             ["model", "training", "prediction"]),

            ("What is training?",
             ["training", "data", "model"]),

            ("What is inference?",
             ["inference", "model", "prediction"]),

            ("What is natural language processing?",
             ["nlp", "language", "text"]),

            ("What is computer vision?",
             ["computer", "vision", "image"]),

            ("What is a chatbot?",
             ["chatbot", "conversation", "ai"]),

            ("What is generative AI?",
             ["generative", "ai", "content"]),

            ("What is a prompt?",
             ["prompt", "ai", "model"])
        ],

        "Medium": [
            ("Explain neural network architecture.",
             ["neural", "network", "layer"]),

            ("What is backpropagation?",
             ["backpropagation", "gradient", "network"]),

            ("What is an activation function?",
             ["activation", "relu", "sigmoid"]),

            ("Explain CNNs.",
             ["cnn", "convolution", "image"]),

            ("Explain RNNs.",
             ["rnn", "sequence", "recurrent"]),

            ("What are transformers?",
             ["transformer", "attention", "nlp"]),

            ("Explain attention mechanism.",
             ["attention", "transformer", "query"]),

            ("What is an embedding?",
             ["embedding", "vector", "text"]),

            ("What is fine-tuning?",
             ["fine", "tuning", "model"]),

            ("What is transfer learning?",
             ["transfer", "learning", "model"]),

            ("Explain tokenization.",
             ["tokenization", "token", "text"]),

            ("What is model evaluation?",
             ["evaluation", "model", "metric"])
        ],

        "Hard": [
            ("Explain transformer architecture in detail.",
             ["transformer", "attention", "encoder", "decoder"]),

            ("Explain self-attention mathematically.",
             ["self", "attention", "query", "key", "value"]),

            ("How does an LLM generate text?",
             ["llm", "token", "generation", "transformer"]),

            ("Explain retrieval augmented generation.",
             ["rag", "retrieval", "generation", "embedding"]),

            ("How would you reduce hallucinations in AI systems?",
             ["hallucination", "rag", "grounding"]),

            ("Explain vector databases.",
             ["vector", "database", "embedding"]),

            ("How do you evaluate a generative AI application?",
             ["evaluation", "generative", "ai", "metric"]),

            ("Explain prompt engineering.",
             ["prompt", "engineering", "instruction"]),

            ("How would you deploy an AI model at scale?",
             ["deployment", "scaling", "model"]),

            ("Explain model quantization.",
             ["quantization", "model", "inference"]),

            ("How do you monitor AI systems in production?",
             ["monitoring", "ai", "production"]),

            ("How would you design an AI interview system?",
             ["ai", "interview", "system", "architecture"])
        ]
    },


    # =========================================================
    # DEVOPS ENGINEER
    # =========================================================

    "DevOps Engineer": {

        "Easy": [
            ("What is DevOps?",
             ["devops", "development", "operations"]),

            ("What is CI/CD?",
             ["ci", "cd", "pipeline"]),

            ("What is Git?",
             ["git", "version", "control"]),

            ("What is Docker?",
             ["docker", "container", "image"]),

            ("What is a container?",
             ["container", "docker", "application"]),

            ("What is Jenkins?",
             ["jenkins", "ci", "pipeline"]),

            ("What is Linux?",
             ["linux", "operating", "system"]),

            ("What is a shell script?",
             ["shell", "script", "linux"]),

            ("What is cloud computing?",
             ["cloud", "server", "computing"]),

            ("What is deployment?",
             ["deployment", "application", "server"]),

            ("What is monitoring?",
             ["monitoring", "logs", "metrics"]),

            ("What is version control?",
             ["version", "git", "control"])
        ],

        "Medium": [
            ("Explain CI/CD pipeline.",
             ["ci", "cd", "pipeline"]),

            ("Explain Docker images and containers.",
             ["docker", "image", "container"]),

            ("What is Docker Compose?",
             ["docker", "compose", "container"]),

            ("What is Kubernetes?",
             ["kubernetes", "container", "cluster"]),

            ("What is infrastructure as code?",
             ["infrastructure", "code", "terraform"]),

            ("What is Terraform?",
             ["terraform", "infrastructure", "cloud"]),

            ("Explain load balancing.",
             ["load", "balancing", "server"]),

            ("What is auto scaling?",
             ["auto", "scaling", "cloud"]),

            ("Explain blue-green deployment.",
             ["blue", "green", "deployment"]),

            ("Explain rolling deployment.",
             ["rolling", "deployment", "update"]),

            ("What is container orchestration?",
             ["container", "orchestration", "kubernetes"]),

            ("How do you monitor applications?",
             ["monitoring", "metrics", "logs"])
        ],

        "Hard": [
            ("Design a production CI/CD pipeline.",
             ["ci", "cd", "pipeline", "deployment"]),

            ("Explain Kubernetes architecture.",
             ["kubernetes", "cluster", "node", "pod"]),

            ("What is Kubernetes service discovery?",
             ["kubernetes", "service", "discovery"]),

            ("Explain Kubernetes deployments.",
             ["deployment", "pod", "kubernetes"]),

            ("How do you implement zero-downtime deployment?",
             ["deployment", "zero", "downtime"]),

            ("Explain DevSecOps.",
             ["devsecops", "security", "pipeline"]),

            ("How do you secure Docker containers?",
             ["docker", "security", "container"]),

            ("How would you handle infrastructure failures?",
             ["failure", "infrastructure", "recovery"]),

            ("Explain observability.",
             ["observability", "logs", "metrics", "traces"]),

            ("How would you design highly available infrastructure?",
             ["high", "availability", "infrastructure"]),

            ("Explain disaster recovery.",
             ["disaster", "recovery", "backup"]),

            ("How do you optimize cloud infrastructure costs?",
             ["cloud", "cost", "optimization"])
        ]
    },


    # =========================================================
    # CLOUD ENGINEER
    # =========================================================

    "Cloud Engineer": {

        "Easy": [
            ("What is cloud computing?",
             ["cloud", "computing", "server"]),

            ("What are the main cloud service models?",
             ["iaas", "paas", "saas"]),

            ("What is virtualization?",
             ["virtualization", "virtual", "machine"]),

            ("What is a virtual machine?",
             ["virtual", "machine", "server"]),

            ("What is cloud storage?",
             ["cloud", "storage", "data"]),

            ("What is a cloud region?",
             ["region", "cloud", "location"]),

            ("What is an availability zone?",
             ["availability", "zone", "cloud"]),

            ("What is a load balancer?",
             ["load", "balancer", "traffic"]),

            ("What is auto scaling?",
             ["auto", "scaling", "cloud"]),

            ("What is IAM?",
             ["iam", "identity", "access"]),

            ("What is a cloud database?",
             ["database", "cloud", "storage"]),

            ("What is serverless computing?",
             ["serverless", "function", "cloud"])
        ],

        "Medium": [
            ("Explain IaaS, PaaS and SaaS.",
             ["iaas", "paas", "saas"]),

            ("Explain cloud networking.",
             ["network", "cloud", "vpc"]),

            ("What is a VPC?",
             ["vpc", "network", "cloud"]),

            ("What is a subnet?",
             ["subnet", "network", "vpc"]),

            ("Explain security groups.",
             ["security", "group", "firewall"]),

            ("What is object storage?",
             ["object", "storage", "bucket"]),

            ("Explain cloud monitoring.",
             ["monitoring", "cloud", "metrics"]),

            ("What is cloud migration?",
             ["migration", "cloud", "application"]),

            ("What is containerization?",
             ["container", "docker", "cloud"]),

            ("What is cloud backup?",
             ["backup", "cloud", "data"]),

            ("Explain cloud load balancing.",
             ["load", "balancer", "cloud"]),

            ("What is infrastructure as code?",
             ["infrastructure", "code", "terraform"])
        ],

        "Hard": [
            ("Design a highly available cloud architecture.",
             ["high", "availability", "cloud", "architecture"]),

            ("Explain multi-region architecture.",
             ["multi", "region", "cloud"]),

            ("How would you design cloud disaster recovery?",
             ["disaster", "recovery", "cloud"]),

            ("Explain cloud cost optimization.",
             ["cost", "optimization", "cloud"]),

            ("How do you secure cloud infrastructure?",
             ["security", "iam", "cloud"]),

            ("Explain zero-trust cloud security.",
             ["zero", "trust", "security"]),

            ("How would you migrate a legacy application to cloud?",
             ["migration", "legacy", "cloud"]),

            ("Explain cloud-native architecture.",
             ["cloud", "native", "architecture"]),

            ("What is Kubernetes in cloud environments?",
             ["kubernetes", "cloud", "container"]),

            ("How would you design scalable cloud storage?",
             ["storage", "scaling", "cloud"]),

            ("Explain cloud observability.",
             ["observability", "logs", "metrics"]),

            ("How would you design a secure multi-tier cloud application?",
             ["security", "multi", "tier", "cloud"])
        ]
    },


    # =========================================================
    # CYBERSECURITY ENGINEER
    # =========================================================

    "Cybersecurity Engineer": {

        "Easy": [
            ("What is cybersecurity?",
             ["cybersecurity", "security", "data"]),

            ("What is authentication?",
             ["authentication", "identity", "login"]),

            ("What is authorization?",
             ["authorization", "permission", "access"]),

            ("What is a firewall?",
             ["firewall", "network", "security"]),

            ("What is malware?",
             ["malware", "virus", "security"]),

            ("What is phishing?",
             ["phishing", "email", "security"]),

            ("What is encryption?",
             ["encryption", "data", "security"]),

            ("What is a password hash?",
             ["hash", "password", "security"]),

            ("What is HTTPS?",
             ["https", "tls", "security"]),

            ("What is a VPN?",
             ["vpn", "network", "security"]),

            ("What is antivirus software?",
             ["antivirus", "malware", "security"]),

            ("What is a security vulnerability?",
             ["vulnerability", "security", "risk"])
        ],

        "Medium": [
            ("Explain symmetric and asymmetric encryption.",
             ["symmetric", "asymmetric", "encryption"]),

            ("What is TLS?",
             ["tls", "encryption", "https"]),

            ("What is SQL injection?",
             ["sql", "injection", "security"]),

            ("What is XSS?",
             ["xss", "script", "security"]),

            ("What is CSRF?",
             ["csrf", "request", "security"]),

            ("What is penetration testing?",
             ["penetration", "testing", "security"]),

            ("What is vulnerability scanning?",
             ["vulnerability", "scanning", "security"]),

            ("What is multi-factor authentication?",
             ["mfa", "authentication", "security"]),

            ("Explain least privilege.",
             ["least", "privilege", "access"]),

            ("What is intrusion detection?",
             ["intrusion", "detection", "network"]),

            ("What is SIEM?",
             ["siem", "security", "logs"]),

            ("How do you secure APIs?",
             ["api", "security", "authentication"])
        ],

        "Hard": [
            ("Design a secure web application architecture.",
             ["security", "web", "architecture"]),

            ("How would you prevent SQL injection?",
             ["sql", "injection", "prepared"]),

            ("How would you prevent XSS attacks?",
             ["xss", "sanitization", "security"]),

            ("Explain zero-trust security.",
             ["zero", "trust", "security"]),

            ("How do you respond to a security incident?",
             ["incident", "response", "security"]),

            ("Explain threat modeling.",
             ["threat", "modeling", "security"]),

            ("What is a security information event management system?",
             ["siem", "event", "security"]),

            ("How do you secure cloud applications?",
             ["cloud", "security", "iam"]),

            ("Explain public key infrastructure.",
             ["pki", "certificate", "encryption"]),

            ("How would you secure authentication systems?",
             ["authentication", "password", "mfa"]),

            ("Explain vulnerability management.",
             ["vulnerability", "management", "security"]),

            ("How do you detect and prevent data breaches?",
             ["data", "breach", "security"])
        ]
    },


    # =========================================================
    # SQL / DATABASE DEVELOPER
    # =========================================================

    "SQL / Database Developer": {

        "Easy": [
            ("What is SQL?",
             ["sql", "query", "database"]),

            ("What is a database?",
             ["database", "data", "storage"]),

            ("What is a table?",
             ["table", "row", "column"]),

            ("What is a primary key?",
             ["primary", "key", "unique"]),

            ("What is a foreign key?",
             ["foreign", "key", "relationship"]),

            ("What is SELECT?",
             ["select", "sql", "query"]),

            ("What is INSERT?",
             ["insert", "sql", "data"]),

            ("What is UPDATE?",
             ["update", "sql", "data"]),

            ("What is DELETE?",
             ["delete", "sql", "data"]),

            ("What is a NULL value?",
             ["null", "sql", "value"]),

            ("What is a database constraint?",
             ["constraint", "database", "key"]),

            ("What is a database index?",
             ["index", "database", "query"])
        ],

        "Medium": [
            ("Explain INNER JOIN.",
             ["inner", "join", "sql"]),

            ("Explain LEFT JOIN.",
             ["left", "join", "sql"]),

            ("What is GROUP BY?",
             ["group", "by", "sql"]),

            ("What is HAVING?",
             ["having", "sql", "group"]),

            ("What is a subquery?",
             ["subquery", "sql", "query"]),

            ("What is normalization?",
             ["normalization", "database", "table"]),

            ("What is denormalization?",
             ["denormalization", "database", "performance"]),

            ("Explain database transactions.",
             ["transaction", "commit", "rollback"]),

            ("What is ACID?",
             ["acid", "atomicity", "consistency"]),

            ("What is a stored procedure?",
             ["stored", "procedure", "sql"]),

            ("What is a view?",
             ["view", "database", "query"]),

            ("How do indexes improve performance?",
             ["index", "performance", "query"])
        ],

        "Hard": [
            ("How do you optimize a slow SQL query?",
             ["sql", "query", "optimization", "index"]),

            ("Explain database indexing strategies.",
             ["index", "database", "performance"]),

            ("Explain transaction isolation levels.",
             ["transaction", "isolation", "database"]),

            ("What is database deadlock?",
             ["deadlock", "transaction", "database"]),

            ("Explain database replication.",
             ["replication", "database", "primary"]),

            ("What is database sharding?",
             ["sharding", "database", "scaling"]),

            ("How would you design a scalable database?",
             ["database", "scaling", "architecture"]),

            ("Explain query execution plans.",
             ["query", "execution", "plan"]),

            ("How do you handle millions of database records?",
             ["database", "large", "records", "index"]),

            ("Explain partitioning.",
             ["partition", "database", "table"]),

            ("How do you ensure database security?",
             ["database", "security", "access"]),

            ("How do you design a high availability database?",
             ["high", "availability", "database"])
        ]
    },


    # =========================================================
    # QA / TEST ENGINEER
    # =========================================================

    "QA / Test Engineer": {

        "Easy": [
            ("What is software testing?",
             ["testing", "software", "quality"]),

            ("What is manual testing?",
             ["manual", "testing", "software"]),

            ("What is automation testing?",
             ["automation", "testing", "software"]),

            ("What is a test case?",
             ["test", "case", "steps"]),

            ("What is a test scenario?",
             ["test", "scenario", "requirement"]),

            ("What is a bug?",
             ["bug", "defect", "software"]),

            ("What is regression testing?",
             ["regression", "testing", "bug"]),

            ("What is functional testing?",
             ["functional", "testing", "requirement"]),

            ("What is smoke testing?",
             ["smoke", "testing", "build"]),

            ("What is sanity testing?",
             ["sanity", "testing", "build"]),

            ("What is SDLC?",
             ["sdlc", "development", "software"]),

            ("What is STLC?",
             ["stlc", "testing", "software"])
        ],

        "Medium": [
            ("Explain test case design.",
             ["test", "case", "design"]),

            ("What is boundary value analysis?",
             ["boundary", "value", "testing"]),

            ("What is equivalence partitioning?",
             ["equivalence", "partitioning", "testing"]),

            ("What is integration testing?",
             ["integration", "testing", "modules"]),

            ("What is system testing?",
             ["system", "testing", "software"]),

            ("What is acceptance testing?",
             ["acceptance", "testing", "user"]),

            ("What is API testing?",
             ["api", "testing", "request"]),

            ("What is performance testing?",
             ["performance", "load", "testing"]),

            ("What is severity and priority?",
             ["severity", "priority", "bug"]),

            ("Explain defect life cycle.",
             ["defect", "lifecycle", "bug"]),

            ("What is test automation?",
             ["automation", "testing", "script"]),

            ("What is Selenium?",
             ["selenium", "automation", "browser"])
        ],

        "Hard": [
            ("How would you design a complete test strategy?",
             ["test", "strategy", "quality"]),

            ("Explain automation framework architecture.",
             ["automation", "framework", "architecture"]),

            ("How would you design a scalable automation framework?",
             ["automation", "framework", "scalable"]),

            ("Explain Page Object Model.",
             ["page", "object", "model", "selenium"]),

            ("What is data-driven testing?",
             ["data", "driven", "testing"]),

            ("What is keyword-driven testing?",
             ["keyword", "driven", "testing"]),

            ("How do you test REST APIs?",
             ["rest", "api", "testing"]),

            ("How do you handle flaky automation tests?",
             ["flaky", "automation", "test"]),

            ("How do you integrate automated tests into CI/CD?",
             ["automation", "ci", "cd", "testing"]),

            ("Explain performance testing strategy.",
             ["performance", "load", "stress", "testing"]),

            ("How do you prioritize test cases?",
             ["test", "priority", "risk"]),

            ("How would you test a production-critical application?",
             ["testing", "risk", "production", "quality"])
        ]
    }
}


# =============================================================
# QUESTION SELECTION FUNCTION
# =============================================================

def get_questions(role, difficulty, count=10):

    role_questions = QUESTIONS.get(
        role,
        {}
    )

    available = role_questions.get(
        difficulty,
        []
    )

    if not available:
        return []

    selected = random.sample(
        available,
        min(count, len(available))
    )

    result = []

    for question, keywords in selected:

        result.append({
            "question": question,
            "keywords": keywords,
            "topic": role
        })

    return result