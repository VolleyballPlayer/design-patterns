Abstract Factory Pattern
========================

Abstract Factory is a creational design pattern that lets you produce families of related objects without specifying their concrete classes.

**:( Problem**

Imagine that you’re creating a furniture shop simulator. Your code consists of classes that represent:

1. A family of related products, say: Chair + Sofa + CoffeeTable.

2. Several variants of this family. For example, products Chair + Sofa + CoffeeTable are available in these variants: Modern, Victorian, ArtDeco.

You need a way to create individual furniture objects so that they match other objects of the same family. Customers get quite mad when they receive non-matching furniture.
Also, you don’t want to change existing code when adding new products or families of products to the program. Furniture vendors update their catalogs very often, and you wouldn’t want to change the core code each time it happens.

**:) Solution**

The first thing the Abstract Factory pattern suggests is to explicitly declare interfaces for each distinct product of the product family (e.g., chair, sofa or coffee table). Then you can make all variants of products follow those interfaces. For example, all chair variants can implement the Chair interface; all coffee table variants can implement the CoffeeTable interface, and so on.
The next move is to declare the Abstract Factory—an interface with a list of creation methods for all products that are part of the product family (for example, createChair, createSofa and createCoffeeTable). These methods must return abstract product types represented by the interfaces we extracted previously: Chair, Sofa, CoffeeTable and so on.
Now, how about the product variants? For each variant of a product family, we create a separate factory class based on the AbstractFactory interface. A factory is a class that returns products of a particular kind. For example, the ModernFurnitureFactory can only create ModernChair, ModernSofa and ModernCoffeeTable objects.
The client code has to work with both factories and products via their respective abstract interfaces. This lets you change the type of a factory that you pass to the client code, as well as the product variant that the client code receives, without breaking the actual client code.
Say the client wants a factory to produce a chair. The client doesn’t have to be aware of the factory’s class, nor does it matter what kind of chair it gets. Whether it’s a Modern model or a Victorian-style chair, the client must treat all chairs in the same manner, using the abstract Chair interface. With this approach, the only thing that the client knows about the chair is that it implements the sitOn method in some way. Also, whichever variant of the chair is returned, it’ll always match the type of sofa or coffee table produced by the same factory object.
There’s one more thing left to clarify: if the client is only exposed to the abstract interfaces, what creates the actual factory objects? Usually, the application creates a concrete factory object at the initialization stage. Just before that, the app must select the factory type depending on the configuration or the environment settings.

**Real-World Analogy**

**Applicability**

* Use the Abstract Factory when your code needs to work with various families of related products, but you don’t want it to depend on the concrete classes of those products—they might be unknown beforehand or you simply want to allow for future extensibility. The Abstract Factory provides you with an interface for creating objects from each class of the product family. As long as your code creates objects via this interface, you don’t have to worry about creating the wrong variant of a product which doesn’t match the products already created by your app.

* Consider implementing the Abstract Factory when you have a class with a set of Factory Methods that blur its primary responsibility. In a well-designed program each class is responsible only for one thing. When a class deals with multiple product types, it may be worth extracting its factory methods into a stand-alone factory class or a full-blown Abstract Factory implementation.

**Pros**

* You can be sure that the products you’re getting from a factory are compatible with each other.
* You avoid tight coupling between concrete products and client code.
* Single Responsibility Principle. You can extract the product creation code into one place, making the code easier to support.
* Open/Closed Principle. You can introduce new variants of products without breaking existing client code.

**Cons**

*  The code may become more complicated than it should be, since a lot of new interfaces and classes are introduced along with the pattern.

**Relations with Other Patterns**

* Many designs start by using Factory Method (less complicated and more customizable via subclasses) and evolve toward Abstract Factory, Prototype, or Builder (more flexible, but more complicated).

* Builder focuses on constructing complex objects step by step. Abstract Factory specializes in creating families of related objects. Abstract Factory returns the product immediately, whereas Builder lets you run some additional construction steps before fetching the product.

* Abstract Factory classes are often based on a set of Factory Methods, but you can also use Prototype to compose the methods on these classes.

* Abstract Factory can serve as an alternative to Facade when you only want to hide the way the subsystem objects are created from the client code.

* You can use Abstract Factory along with Bridge. This pairing is useful when some abstractions defined by Bridge can only work with specific implementations. In this case, Abstract Factory can encapsulate these relations and hide the complexity from the client code.

* Abstract Factories, Builders and Prototypes can all be implemented as Singletons.

**How to Implement**

* Map out a matrix of distinct product types versus variants of these products.

* Declare abstract product interfaces for all product types. Then make all concrete product classes implement these interfaces.

* Declare the abstract factory interface with a set of creation methods for all abstract products.

* Implement a set of concrete factory classes, one for each product variant.

* Create factory initialization code somewhere in the app. It should instantiate one of the concrete factory classes, depending on the application configuration or the current environment. Pass this factory object to all classes that construct products.

* Scan through the code and find all direct calls to product constructors. Replace them with calls to the appropriate creation method on the factory object.

**UML of the example implemented in this repository**

.. uml::

    @startuml

        skinparam classAttributeIconSize 0

        left to right direction

        AbstractCoffee <.. AbstractFactory
        AbstractMilk <.. AbstractFactory
        AbstractMilkFoam <.. AbstractFactory
        AbstractChocolate <.. AbstractFactory
        AbstractReceipt <.. AbstractFactory

        AbstractFactory <.. client

        AbstractFactory <|-- LatteFactory
        AbstractFactory <|-- CappuccinoFactory
        AbstractFactory <|-- EspressoFactory

        LatteFactory <.. CoffeeForLatte
        LatteFactory <.. MilkForLatte
        LatteFactory <.. MilkFoamForLatte
        LatteFactory <.. ChocolateForLatte
        LatteFactory <.. ReceiptForLatte
        CappuccinoFactory <.. CoffeeForCappuccino
        CappuccinoFactory <.. MilkForCappuccino
        CappuccinoFactory <.. MilkFoamForCappuccino
        CappuccinoFactory <.. ChocolateForCappuccino
        CappuccinoFactory <.. ReceiptForCappuccino
        EspressoFactory <.. CoffeeForEspresso
        EspressoFactory <.. MilkForEspresso
        EspressoFactory <.. MilkFoamForEspresso
        EspressoFactory <.. ChocolateForEspresso
        EspressoFactory <.. ReceiptForEspresso

        AbstractCoffee <|-- CoffeeForLatte
        AbstractMilk <|-- MilkForLatte
        AbstractMilkFoam <|-- MilkFoamForLatte
        AbstractChocolate <|-- ChocolateForLatte
        AbstractReceipt <|-- ReceiptForLatte
        AbstractCoffee <|-- CoffeeForCappuccino
        AbstractMilk <|-- MilkForCappuccino
        AbstractMilkFoam <|-- MilkFoamForCappuccino
        AbstractChocolate <|-- ChocolateForCappuccino
        AbstractReceipt <|-- ReceiptForCappuccino
        AbstractCoffee <|-- CoffeeForEspresso
        AbstractMilk <|-- MilkForEspresso
        AbstractMilkFoam <|-- MilkFoamForEspresso
        AbstractChocolate <|-- ChocolateForEspresso
        AbstractReceipt <|-- ReceiptForEspresso

        abstract class AbstractFactory {
        + get_coffee()
        + get_milk()
        + get_milk_foam()
        + get_chocolate()
        + get_coffee_receipt()
        }

        class LatteFactory {
        + get_coffee()
        + get_milk()
        + get_milk_foam()
        + get_chocolate()
        + get_coffee_receipt()
        }

        class CappuccinoFactory {
        + get_coffee()
        + get_milk()
        + get_milk_foam()
        + get_chocolate()
        + get_coffee_receipt()
        }

        class EspressoFactory {
        + get_coffee()
        + get_milk()
        + get_milk_foam()
        + get_chocolate()
        + get_coffee_receipt()
        }

        abstract class AbstractCoffee {
        + get_amount()
        }

        class CoffeeForLatte {
        + get_amount()
        }

        class CoffeeForCappuccino {
        + get_amount()
        }

        class CoffeeForEspresso {
        + get_amount()
        }

        abstract class AbstractMilk {
        + get_amount()
        }

        class MilkForLatte {
        + get_amount()
        }

        class MilkForCappuccino {
        + get_amount()
        }

        class MilkForEspresso {
        + get_amount()
        }

        abstract class AbstractMilkFoam {
        + get_amount()
        }

        class MilkFoamForLatte {
        + get_amount()
        }

        class MilkFoamForCappuccino {
        + get_amount()
        }

        class MilkFoamForEspresso {
        + get_amount()
        }

        abstract class AbstractChocolate {
        + get_amount()
        }

        class ChocolateForLatte {
        + get_amount()
        }

        class ChocolateForCappuccino {
        + get_amount()
        }

        class ChocolateForEspresso {
        + get_amount()
        }

        abstract class AbstractReceipt {
        + get_receipt()
        }

        class ChocolateForLatte {
        + get_receipt()
        }

        class ChocolateForCappuccino {
        + get_receipt()
        }

        class ChocolateForEspresso {
        + get_receipt()
        }

        hide client circle

    @enduml
