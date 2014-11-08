#include <iostream>

// (Imperfect) Double dispatch emulation using virtual functions only
// Example taken from Item 31 of More Effective C++ by Scott Meyers

// The flaw of this design is that as new subclasses of GameObject are added, each class definition should be
// amended to include a new collide virtual method.

class SpaceShip;
class Asteroid;

class GameObject
{
public:
    virtual void collide(GameObject& other) = 0;
    virtual void collide(SpaceShip& other) = 0;
    virtual void collide(Asteroid& other) = 0;
};

class SpaceShip : public GameObject
{
public:
    virtual void collide(GameObject& other);
    virtual void collide(SpaceShip& other);
    virtual void collide(Asteroid& other);
};

class Asteroid : public GameObject
{
public:
    virtual void collide(GameObject& other);
    virtual void collide(SpaceShip& other);
    virtual void collide(Asteroid& other);
};

void SpaceShip::collide(GameObject& other)
{
    std::cout << "SpaceShip::collide()\n";

    // Second dispatch.
    // If other is SpaceShip will call SpaceShip::collide(SpaceShip&)
    // If other is Asteroid will call Asteroid::collide(SpaceShip&)
    other.collide(*this);
}

void SpaceShip::collide(SpaceShip& other)
{
    std::cout << "SpaceShip - SpaceShip\n";
}

void SpaceShip::collide(Asteroid& other)
{
    std::cout << "SpaceShip - Asteroid\n";
}

void Asteroid::collide(GameObject& other)
{
    std::cout << "Asteroid::collide()\n";
    
    // Second dispatch
    // If other is SpaceShip will call SpaceShip::collide(Asteroid&)
    // If other is Asteroid will call Asteroid::collide(Asteroid&)
    other.collide(*this);
}

void Asteroid::collide(SpaceShip& other)
{
    std::cout << "Asteroid - SpaceShip\n";
}

void Asteroid::collide(Asteroid& other)
{
    std::cout << "Asteroid - Asteroid\n";
}

void collide(GameObject& obj1, GameObject& obj2)
{
    // First dispatch
    // If obj1 is SpaceShip will call SpaceShip::collide(GameObject&)
    // If obj1 is Asteroid will call Asteroid::collide(GameObject&)
    // Note that real type of obj2 is not used to decide which overloaded method should be called
    obj1.collide(obj2);
}

int main()
{
    SpaceShip spaceShip;
    Asteroid asteroid;

    collide(spaceShip, spaceShip);
    collide(spaceShip, asteroid);
    collide(asteroid, spaceShip);
    collide(asteroid, asteroid);
    
    return 0;
}

