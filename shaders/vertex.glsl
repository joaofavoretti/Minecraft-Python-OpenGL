#version 460 core

// Attribute locations
layout (location = 0) in vec3 aPosition;
layout (location = 1) in vec2 aTexCoord;

// Uniform locations
uniform mat4 uTransform;
uniform mat4 uView;
uniform mat4 uProjection;

out vec2 vTexCoord;

void main()
{
    gl_Position = uProjection * uView * uTransform * vec4(aPosition, 1.0);
    vTexCoord = aTexCoord;
}
