# Ports and Adapters Pattern (Hexagonal Architecture)

The **Ports and Adapters** pattern, also known as **Hexagonal Architecture**, is a software design pattern that isolates core business logic from external dependencies such as databases, APIs, user interfaces, and other services.

## Overview

The pattern separates concerns into three main components:

1. **Core Domain** (Business Logic)
   - Contains the essential business rules and domain models
   - Independent of external systems
   - No direct dependencies on frameworks or infrastructure

2. **Ports** (Interfaces)
   - Abstract interfaces that define how the core domain interacts with the outside world
   - Input ports (driving/primary): how the application is used (e.g., API handlers, CLI)
   - Output ports (driven/secondary): how the application uses external systems (e.g., databases, messaging)

3. **Adapters** (Implementations)
   - Concrete implementations of ports
   - Translate between the domain and external systems
   - Can be easily swapped without changing core logic

## Benefits

✅ **Testability**: Easily swap real dependencies for test doubles (mocks, stubs)  
✅ **Flexibility**: Change implementations without touching business logic  
✅ **Maintainability**: Clear boundaries between layers  
✅ **Independence**: Core logic doesn't depend on frameworks or external libraries  
✅ **Parallel Development**: Teams can work on adapters independently

## Examples Included

This sample demonstrates four different approaches:

### 1. User Repository Pattern (ABC-based)
Classic repository pattern with:
- Abstract base class defining the port
- Multiple adapters: in-memory and file-based storage
- Core service depending only on the port

### 2. Notification Service (Protocol-based)
Python's structural subtyping approach:
- Protocol interface (duck typing)
- Multiple notification channels: email, SMS, console
- No inheritance required

### 3. Payment Gateway
Swappable payment processors:
- Multiple payment gateways: Stripe, PayPal, Mock
- Core payment service isolated from gateway details

### 4. Logger Port (Callable approach)
Lightweight functional approach:
- Type alias for simple ports
- Adapters as functions
- Console, file, and null loggers

## Usage

Run the example:

```bash
python3 samples/dsa/ports_adapters/ports_adapters.py
```

## When to Use This Pattern

✅ **Good fit:**
- Applications with multiple data sources or external integrations
- Systems requiring high testability
- Projects where requirements change frequently
- Microservices and modular monoliths

⚠️ **Overkill for:**
- Simple scripts or one-off utilities
- Applications with stable, single external dependencies
- Prototypes or proof-of-concept code

## Key Principles

1. **Dependency Inversion**: Core domain depends on abstractions (ports), not concrete implementations
2. **Single Responsibility**: Each adapter handles one specific external system
3. **Open/Closed**: Easy to add new adapters without modifying existing code
4. **Interface Segregation**: Ports define minimal, focused interfaces

## Python-Specific Approaches

Python offers multiple ways to implement this pattern:

| Approach | When to Use |
|----------|-------------|
| **ABC (Abstract Base Class)** | Need explicit contracts enforced at class definition time |
| **Protocol** | Prefer duck typing without inheritance |
| **Callable/Type Alias** | Simple, stateless ports (functional approach) |

## Further Reading

- [Hexagonal Architecture (Alistair Cockburn)](https://alistair.cockburn.us/hexagonal-architecture/)
- [Clean Architecture (Robert C. Martin)](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html)
- [Ports & Adapters Pattern](https://softwarecampament.wordpress.com/portsadapters/)
