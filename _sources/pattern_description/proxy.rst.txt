Proxy
=====

Proxy is a structural design pattern that lets you provide a substitute or placeholder for another object. A proxy controls access to the original object, allowing you to perform something either before or after the request gets through to the original object.

**:( Problem**

Why would you want to control access to an object? Here is an example: you have a massive object that consumes a vast amount of system resources. You need it from time to time, but not always.

You could implement lazy initialization: create this object only when it’s actually needed. All of the object’s clients would need to execute some deferred initialization code. Unfortunately, this would probably cause a lot of code duplication.

In an ideal world, we’d want to put this code directly into our object’s class, but that isn’t always possible. For instance, the class may be part of a closed 3rd-party library.

**:) Solution**

The Proxy pattern suggests that you create a new proxy class with the same interface as an original service object. Then you update your app so that it passes the proxy object to all of the original object’s clients. Upon receiving a request from a client, the proxy creates a real service object and delegates all the work to it.

But what’s the benefit? If you need to execute something either before or after the primary logic of the class, the proxy lets you do this without changing that class. Since the proxy implements the same interface as the original class, it can be passed to any client that expects a real service object.

**Real-World Analogy**

A credit card is a proxy for a bank account, which is a proxy for a bundle of cash. Both implement the same interface: they can be used for making a payment. A consumer feels great because there’s no need to carry loads of cash around. A shop owner is also happy since the income from a transaction gets added electronically to the shop’s bank account without the risk of losing the deposit or getting robbed on the way to the bank.

**Applicability**

There are dozens of ways to utilize the Proxy pattern. Let’s go over the most popular uses.

 Lazy initialization (virtual proxy). This is when you have a heavyweight service object that wastes system resources by being always up, even though you only need it from time to time.

 Instead of creating the object when the app launches, you can delay the object’s initialization to a time when it’s really needed.

 Access control (protection proxy). This is when you want only specific clients to be able to use the service object; for instance, when your objects are crucial parts of an operating system and clients are various launched applications (including malicious ones).

 The proxy can pass the request to the service object only if the client’s credentials match some criteria.

 Local execution of a remote service (remote proxy). This is when the service object is located on a remote server.

 In this case, the proxy passes the client request over the network, handling all of the nasty details of working with the network.

 Logging requests (logging proxy). This is when you want to keep a history of requests to the service object.

 The proxy can log each request before passing it to the service.

 Caching request results (caching proxy). This is when you need to cache results of client requests and manage the life cycle of this cache, especially if results are quite large.

 The proxy can implement caching for recurring requests that always yield the same results. The proxy may use the parameters of requests as the cache keys.

 Smart reference. This is when you need to be able to dismiss a heavyweight object once there are no clients that use it.

 The proxy can keep track of clients that obtained a reference to the service object or its results. From time to time, the proxy may go over the clients and check whether they are still active. If the client list gets empty, the proxy might dismiss the service object and free the underlying system resources.

The proxy can also track whether the client had modified the service object. Then the unchanged objects may be reused by other clients.

**Pros**

* You can control the service object without clients knowing about it.
* You can manage the lifecycle of the service object when clients don’t care about it.
* The proxy works even if the service object isn’t ready or is not available.
* Open/Closed Principle. You can introduce new proxies without changing the service or clients.

**Cons**

* The code may become more complicated since you need to introduce a lot of new classes.
* The response from the service might get delayed.

**Relations with Other Patterns**

* With Adapter you access an existing object via different interface. With Proxy, the interface stays the same. With Decorator you access the object via an enhanced interface.

* Facade is similar to Proxy in that both buffer a complex entity and initialize it on its own. Unlike Facade, Proxy has the same interface as its service object, which makes them interchangeable.

* Decorator and Proxy have similar structures, but very different intents. Both patterns are built on the composition principle, where one object is supposed to delegate some of the work to another. The difference is that a Proxy usually manages the life cycle of its service object on its own, whereas the composition of Decorators is always controlled by the client.

**How to Implement**

* If there’s no pre-existing service interface, create one to make proxy and service objects interchangeable. Extracting the interface from the service class isn’t always possible, because you’d need to change all of the service’s clients to use that interface. Plan B is to make the proxy a subclass of the service class, and this way it’ll inherit the interface of the service.

* Create the proxy class. It should have a field for storing a reference to the service. Usually, proxies create and manage the whole life cycle of their services. On rare occasions, a service is passed to the proxy via a constructor by the client.

* Implement the proxy methods according to their purposes. In most cases, after doing some work, the proxy should delegate the work to the service object.

* Consider introducing a creation method that decides whether the client gets a proxy or a real service. This can be a simple static method in the proxy class or a full-blown factory method.

* Consider implementing lazy initialization for the service object.

**UML of the example implemented in this repository**

.. uml::

    @startuml

        skinparam classAttributeIconSize 0

        Subject <-- client
        Subject <|.. Coffee
        Subject <|.. Proxy

        abstract class Subject {
        + request()
        }

        class Coffee {
        + request()
        }

        class Proxy {
        - real_subject
        - cache
        + request()
        + should_prepare_coffee()
        + log_access()
        }

        hide client circle

    @enduml
