#include <cmath>

class Filter
{
protected:
    float prevVal;

public:
    virtual float filter(float value, float time) {
        prevVal = value;
        return value;
    }

    Filter() : prevVal(0) {}

    virtual ~Filter() {}
};

class SimpleFilter : public Filter
{
protected:
    float iRadius;

public:
    float filter(float value, float time) override {
        if (std::fabs(value - prevVal) < iRadius) {
            value = prevVal;
        }

        return Filter::filter(value, time);
    }

    SimpleFilter(float innerRadius) : Filter(), iRadius(innerRadius) {}
};


class RadialFilter : public SimpleFilter
{
protected:
    float oRadius;
    float descentSpeed;

public:
    float filter(float value, float time) override {
        float distance = prevVal - value;

        if (std::fabs(distance) < iRadius) {
            value = prevVal;
        }

        else if (std::fabs(distance) < oRadius) {  
            // Apply a curve that slows down as it gets closer
            //value = prevVal + distance * descentSpeed * time;  

            //Apply linear amount of movement (Should be a better way that doesnt need if statement)
            if (distance < 0)
            {
                value = prevVal + (1 - descentSpeed) * oRadius * time;
            }
            else
            {
                value = prevVal - (1 - descentSpeed) * oRadius * time;
            }
        }

        return Filter::filter(value, time);
    }

    RadialFilter(float innerRadius, float outerRadius, float descentSpeed) 
        : SimpleFilter(innerRadius), oRadius(outerRadius), descentSpeed(descentSpeed) {}
};
