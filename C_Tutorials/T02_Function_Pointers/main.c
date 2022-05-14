#include <stdio.h>
//#include <stdlib.h>
#include <stdbool.h>

typedef enum {
    SBC,
    AAC
} codec_t;

typedef struct{
    int sampleRate;
    bool stereo;
    codec_t codec;
} audioConfig_t;

typedef struct{
    void(* sbc)(int sampleRate, bool stereo);
    void(* aac)(int sampleRate, bool stereo);

} handlers_t;

void handleSBC(int sampleRate, bool stereo){
     printf("%d %d\n", sampleRate, stereo);
}

int main(){
    audioConfig_t* audio = malloc(sizeof(audioConfig_t));
    
    audio->codec = SBC;
    audio->sampleRate = 44000;
    audio->stereo = 1;

    handlers_t handler;
    handler.aac = handleSBC;
    handler.sbc = handleSBC;

    switch (audio->codec)
    {
    case SBC:
        /* code */
        handler.sbc(audio->sampleRate, audio->stereo);
        break;
    case AAC:
        /* code */
        handler.aac(audio->sampleRate, audio->stereo);
        break;
    
    default:
        break;
    }

    free(audio);
    printf("Hello World \n");
    return 0;
}
