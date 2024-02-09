// Pong 2.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include <string>
#include <stdlib.h>
#include <SDL.h>
#include <SDL_ttf.h>
#include <SDL_mixer.h>
#include <SDL_image.h>
#include "Pong 2.h"

const int WIDTH = 1920;
const int HEIGHT = 1080;
const int SPEED = 13;
const int SIZE = 16;
const int BALL_SPEED = 20;
const double PI = 3.14159265358979323846;
const int TIMERDURATION = 120;

using namespace std;

SDL_Renderer* renderer;
SDL_Window* window;

TTF_Font* font;
TTF_Font* fontBig;
TTF_Font* fontSmall;

SDL_Color color;

SDL_Event event;

bool running;
bool repeat;
bool game;
int frameCount, timerFPS, lastFrame, fps;

SDL_Rect leftPaddle, rightPaddle, ball, scoreBoard;
SDL_Rect introRect;
SDL_Rect resultRect;
SDL_Rect timerText;
SDL_Rect buttonRect;

float velX, velY;

string scoreLeft, scoreRight;

int leftScore, rightScore;

bool turn;

bool play;

int startTime;



void serve() 
{
    leftPaddle.x = 32;
    leftPaddle.y = (HEIGHT / 2) - (leftPaddle.h / 2);
    rightPaddle.y = leftPaddle.y;
    rightPaddle.x = WIDTH - rightPaddle.w - 32;
    if (turn) 
    {
        ball.x = leftPaddle.x + (leftPaddle.w * 4);
        velX = BALL_SPEED;
    }
    else 
    {
        ball.x = rightPaddle.x - (rightPaddle.w * 4);
        velX = -BALL_SPEED;
    }
    ball.y = HEIGHT / 2;
    velY = 0;
    turn = !turn;
}

void update() 
{
    if (SDL_HasIntersection(&ball, &leftPaddle)) 
    {
        double rel = (leftPaddle.y + (leftPaddle.h / 2)) - (ball.y + (SIZE / 2));
        double normal = rel / (leftPaddle.h / 2);
        double bounce = normal * (5 * PI / 12);
        velX = BALL_SPEED * cos(bounce);
        velY = BALL_SPEED * -sin(bounce);

        playSound("audio/paddle.mp3", 0, 100);
    }
    if (SDL_HasIntersection(&ball, &rightPaddle))
    {
        double rel = (rightPaddle.y + (rightPaddle.h / 2)) - (ball.y + (SIZE / 2));
        double norm = rel / (rightPaddle.h / 2);
        double bounce = norm * (5 * PI / 12);
        velX = -BALL_SPEED * cos(bounce);
        velY = BALL_SPEED * -sin(bounce);

        playSound("audio/paddle.mp3", 0, 100);
    }
    if (ball.y > (rightPaddle.y + (rightPaddle.h / 2)))
    {
        rightPaddle.y += SPEED;
    }
    if (ball.y < (rightPaddle.y + (rightPaddle.h / 2)))
    {
        rightPaddle.y -= SPEED;
    }
    if (ball.x < 0) 
    {
        rightScore++; 
        serve(); 
        playSound("audio/score.mp3", 0, 20);
    }
    if (ball.x + SIZE > WIDTH) 
    { 
        leftScore++; 
        serve(); 
        playSound("audio/score.mp3", 0, 20);
    }
    if (ball.y<0 || ball.y + SIZE>HEIGHT)
    {
        playSound("audio/wall.mp3", 0, 80);
        velY = -velY;
    }

    ball.x += velX;
    ball.y += velY;

    scoreLeft = to_string(leftScore);
    scoreRight = to_string(rightScore);

    if (leftPaddle.y < 0)
    {
        leftPaddle.y = 0;
    }
    if (leftPaddle.y + leftPaddle.h > HEIGHT)
    {
        leftPaddle.y = HEIGHT - leftPaddle.h;
    }
    if (rightPaddle.y < 0)
    {
        rightPaddle.y = 0;
    }
    if (rightPaddle.y + rightPaddle.h > HEIGHT)
    {
        rightPaddle.y = HEIGHT - rightPaddle.h;
    }
}

void input() 
{
    const Uint8* keystates = SDL_GetKeyboardState(NULL);  
    while (SDL_PollEvent(&event))
    {
        if (event.type == SDL_QUIT) 
        {
            running = false;
        }
            
    }

    if (keystates[SDL_SCANCODE_ESCAPE])
    {
        running = false;
    }
    if (keystates[SDL_SCANCODE_UP])
    {
        leftPaddle.y -= SPEED;
    }
    if (keystates[SDL_SCANCODE_DOWN])
    {
        leftPaddle.y += SPEED;
    }
}

void timer()
{
    int currentTime = SDL_GetTicks();
    int elapsedTime = (currentTime - startTime) / 1000;
    int remainingTime = TIMERDURATION - elapsedTime;

    if (remainingTime < 0) {
        remainingTime = 0;
    }

    string timeText = to_string(remainingTime);

    write(timeText, timerText, 0, +HEIGHT / 2 -HEIGHT/20, font, false);

    if (remainingTime == 0) 
    {
        running = false;
    }

}

void render() 
{
    SDL_SetRenderDrawColor(renderer, 0, 0, 0, 255); /*Black background*/
    SDL_RenderClear(renderer);

    frameCount++;

    int timerFPS = SDL_GetTicks() - lastFrame;

    if (timerFPS < (1000 / 60)) 
    {
        SDL_Delay((1000 / 60) - timerFPS);
    }
    
    SDL_SetRenderDrawColor(renderer, color.r, color.g, color.b, 255); /*White props*/

    imagePost("images/paddle1.png", rightPaddle);
    imagePost("images/paddle1.png", leftPaddle);
    imagePost("images/circle1.png", ball);
    
    write(scoreLeft, scoreBoard, -WIDTH/4, - HEIGHT/2 + HEIGHT/20, font, false);
    write(scoreRight, scoreBoard, +WIDTH/4, -HEIGHT / 2 + HEIGHT / 20, font, false);

    timer();

    SDL_RenderPresent(renderer);
}

void waitKey(int typeCase)
{
    const Uint8* keystates = SDL_GetKeyboardState(NULL);

    switch (typeCase)
    {
        case 1:
            while (SDL_WaitEvent(&event))
            {
                if (event.type == SDL_QUIT)
                {
                    game = false;
                }
                if (event.type == SDL_KEYUP)
                {
                    break;
                }
            }
            break;

        case 2:
            while (SDL_WaitEvent(&event))
            {
                if (keystates[SDL_SCANCODE_ESCAPE])
                {
                    game = false;
                    break;
                }
                if (keystates[SDL_SCANCODE_RETURN])
                {
                    break;
                }
            }
            break;
    }
}

void imagePost(string image, SDL_Rect object)
{
    SDL_Surface* surface;
    SDL_Texture* texture;

    const char* t = image.c_str();

    surface = IMG_Load(t);
    texture = SDL_CreateTextureFromSurface(renderer, surface);

    object.w = surface->w;
    object.h = surface->h;

    SDL_FreeSurface(surface);
    SDL_RenderCopy(renderer, texture, NULL, &object);
    SDL_DestroyTexture(texture);
    /*SDL_RenderPresent(renderer);*/
}

void write(string text, SDL_Rect post, int x, int y, TTF_Font* tempFont, bool presentRender)
{
    SDL_Surface* surface;
    SDL_Texture* texture;

    const char* t = text.c_str();

    SDL_SetRenderDrawColor(renderer, color.r, color.g, color.b, 255);

    surface = TTF_RenderText_Solid(tempFont, t, color);
    texture = SDL_CreateTextureFromSurface(renderer, surface);

    post.w = surface->w;
    post.h = surface->h;

    post.x = WIDTH / 2 - post.w / 2 + x;
    post.y = HEIGHT / 2 - post.h / 2 + y;

    SDL_FreeSurface(surface);
    SDL_RenderCopy(renderer, texture, NULL, &post);
    SDL_DestroyTexture(texture);
    if (presentRender)
    {
        SDL_RenderPresent(renderer);
    }
    else if (!presentRender)
    {
        return;
    }
}

void playSound(string sound, int loopN, int volume)
{
    const char* s = sound.c_str();
    Mix_Music* music = Mix_LoadMUS(s);

    Mix_VolumeMusic(volume);

    Mix_PlayMusic(music, loopN);
}

void endScreenWinner(string result) 
{
    write(result, resultRect, 0, 0, fontBig, true);

    string retry = "press ENTER to play again";
    write(retry, resultRect, 0, + HEIGHT/6, fontSmall, true);
    string quit = "press ESC to quit game";
    write(quit, resultRect, 0, + HEIGHT/4, fontSmall, true);
}
void introScreen()
{
    playSound("audio/intro.mp3", -1, 40);

    string introText = "Press any key to begin...";
    write(introText, introRect, 0, +HEIGHT / 10, font, true);
    waitKey(1);
    string introTitle = "PONG 2";
    write(introTitle, introRect, 0, -HEIGHT / 10, fontBig, true);
    waitKey(1);
    string introCredit = "Guidi Cordero Carlos Emilio";
    write(introCredit, introRect, +WIDTH / 2 - WIDTH / 9, +HEIGHT / 2 - HEIGHT / 20, fontSmall, true);
    waitKey(1);
}

void winnerDetermine()
{
    if (leftScore > rightScore)
    {
        endScreenWinner("YOU WIN!!!");
        playSound("audio/win.mp3", -1, 40);
        waitKey(2);
    }

    else if (leftScore < rightScore)
    {
        endScreenWinner("YOU LOOSE :C");
        playSound("audio/loose.mp3", -1, 60);
        waitKey(2);
    }

    else if (leftScore == rightScore)
    {
        endScreenWinner("DRAW¿?");
        playSound("audio/draw.mp3", -1, 40);
        waitKey(2);
    }
}

int main(int argc, char* args[]){
    if (SDL_Init(SDL_INIT_EVERYTHING) < 0) 
    {
        cout << "Failed at SDL_Init()" << endl;
    }

    if (SDL_CreateWindowAndRenderer(WIDTH, HEIGHT, 0, &window, &renderer) < 0) 
    {
        cout << "Failed at SDL_CreateWindowAndRenderer()" << endl;
    }

    SDL_SetWindowTitle(window, "Pong 2");

    TTF_Init();

    Mix_Init(MIX_INIT_MP3);
    Mix_OpenAudio(48000, AUDIO_S16SYS, 2, 2048);

    font = TTF_OpenFont("fonts/Minecraftia-Regular.ttf", 32);
    fontBig = TTF_OpenFont("fonts/Minecraftia-Regular.ttf", 50);
    fontSmall = TTF_OpenFont("fonts/Minecraftia-Regular.ttf", 24);

    game = true;

    while (game) /*game restart*/
    {
        leftScore = rightScore = 0;
        leftPaddle.x = 32; leftPaddle.h = HEIGHT / 4; leftPaddle.y = (HEIGHT / 2) - (leftPaddle.h / 2); leftPaddle.w = 12;
        rightPaddle = leftPaddle; rightPaddle.x = WIDTH - rightPaddle.w - 32;
        color.r = 255;
        color.g = 255;
        color.b = 255;
        ball.w = ball.h = SIZE;

        SDL_SetRenderDrawColor(renderer, 0, 0, 0, 255); /*reset render*/
        SDL_RenderClear(renderer);
        Mix_HaltMusic();
        introScreen();
        Mix_HaltMusic();
        serve();

        running = true;

        int lastTime = 0;
        startTime = SDL_GetTicks(); /*timer start*/

        while (running)
        {
            lastFrame = SDL_GetTicks();
            if (lastFrame >= (lastTime + 1000))
            {
                lastTime = lastFrame;
                fps = frameCount;
                frameCount = 0;

            }
            update();
            input();
            render();
        }
        winnerDetermine();
    }

    TTF_CloseFont(font);
    SDL_DestroyRenderer(renderer);
    SDL_DestroyWindow(window);
    SDL_Quit();

    return 0;
}