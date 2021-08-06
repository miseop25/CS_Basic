# IPC(Interprocess Communication) - PIPE

## IPC, 프로세스간 통신이란? 

IPC(Interprocess Commnuication)는 말 그대로 프로세스간애   
데이터를 주고받는 행위를 말한다! 우리가 소통하듯이 말이다.    

이번 포스팅에서는 IPC 중에서 PIPE 통신과 관련된 것을 진행하고자 한다.(IPC 통신의 종류는 다양하다.)    


*** 

## PIPE(파이프)    

파이프를 활용한 통신 방법은 IPC 중에서 가장 간단한 통신 방법중 하나이다.    
간단한 그림을 통해 살펴보면 이해가 조금 더 빠를 수 있을 것 같다.   

![스크린샷 2021-08-05 오후 12 13 17](https://user-images.githubusercontent.com/44546283/128285161-3f0b9c4d-65f3-4c6e-80e9-e5933767bdbb.png)

우리가 현실에서 보는 파이프처럼 저런 관을 통해서 데이터를 주고 받을 수 있다.  

### 파이프의 특징과 장단점   

    특징 
    - 파이프는 두개의 프로세스를 연결하고 하나의 프로세스는 데이터를 쓰기만 하고    
      다른 프로세스는 데이터를 읽으수만 있다. 
    - 두 프로세스 모두 읽기/쓰기를 하고 싶다면 두개의 파이프를 만들어야 가능하다.  
    - read()와 write()가 기본적으로 block mode로 작동되어 프로세스가 Read 대기중이라면   
      read가 끝나기 전에는 write를 할 수 없다. 
    
    장점  
    - 단순하여 간단하게 사용 할 수 있다.   
    
    단점 
    - 두 프로세스가 서로를 명확하게 알고 있어야 한다.(그래서 부모 자식 프로세스에서 많이 사용)
    - 양방향 통신을 하려고 한다면 두개의 파이프를 만들어야 하기 때문에 구현이 다소 복잡해질 수 있다.   
    - Buffer가 상대적으로 작기 때문에 Overflow가 날 확률이 높다.   


간단하게 파이프의 개념과 장단점에 대해서 살펴봤는데 서로 생판 모르는 프로세스끼리는 통신을 진행할 수 없다는 큰 문제가 있다.   
하지만 걱정할 필요 없다! 서로 몰라도 사용가능한 Named PIPE라는 것이 존재한다.   


## Named PIPE   

Named PIPE 는 말 그대로 위에서 소개한 파이프에 이름이 있는 것이다.   
위의 파이프는 식별하는 이름이 없어서 두 프로세스가 누구인지 확실히 알 수 있을때 사용할 수 있는 반면  
Named 파이프는 파이프 이름만 알고 있다면 전혀 상관없는 프로세스간에도 통신이 가능하다.   

![스크린샷 2021-08-05 오후 12 47 09](https://user-images.githubusercontent.com/44546283/128287784-2c88dc0d-5e9b-4c9f-aabc-b52d0c280a1a.png)   

하지만 Named 파이프도 기본적으로 파이프 구조이기 때문에 위에서 말한 파이프와 유사한 특징을 가지고 있다.   
즉, 양방향으로 통신을 하고 싶다면 두개의 파이프가 존재해야 한다.   



업무를 진행하다 프로세스간 통신 중 Named 파이프를 알아볼 일이 있어서 간략하게 정리해 보았습니다.  


## Named Pipe를 활용한 간단한 예제 

Pipe가 대략적으로 무엇인지는 알겠지만 어떻게 사용하지? 라는 의문이 있을 것 같아 간단한 예제를 준비했습니다.   

서버, 클라이언트로 구성되어있고 클라이언트에서 메세지를 주면 서버에서 받아서 출력하는 기능을 하는 예제입니다.    

<img src="https://user-images.githubusercontent.com/44546283/128348946-94b4d4a6-583c-4365-994a-9408a8f57a4a.png" width="600" height="300">

대략 적인 메시지 흐름은 다음과 같습니다.   

#### Server Code 
```
#include "windows.h"
#include <iostream> 
#include <tchar.h>
#include <string.h>

#define PipeName _T("\\\\.\\pipe\\testPipe")  //파이프의 이름 명시 


#define BUFFER_SIZE 1024 //1k
#define ACK_MESG_RECV "Message received successfully"


HANDLE hPipe;

int repeate() {
	char szBuffer[BUFFER_SIZE];
	DWORD cbBytes;


	//Read client message
	BOOL bResult = ReadFile(
		hPipe,                // handle to pipe 
		szBuffer,             // buffer to receive data 
		sizeof(szBuffer),     // size of buffer 
		&cbBytes,             // number of bytes read 
		NULL);                // not overlapped I/O 

	if ((!bResult) || (0 == cbBytes))
	{
		printf("\nError occurred while reading from the client: %d", GetLastError());
		CloseHandle(hPipe);
		system("Pause");
		return 1;  //Error
	}
	else
	{
		printf("\nReadFile() was successful.");
	}

	printf("\nClient sent the following message: %s", szBuffer);

	strcpy_s(szBuffer, ACK_MESG_RECV);


	repeate();

}


int main(int argc, char* argv[])
{
	hPipe = CreateNamedPipe(
		PipeName,             // pipe name 
		PIPE_ACCESS_DUPLEX,       // read/write access 
		PIPE_TYPE_MESSAGE |       // message type pipe 
		PIPE_READMODE_MESSAGE |   // message-read mode 
		PIPE_WAIT,                // blocking mode 
		PIPE_UNLIMITED_INSTANCES, // max. instances  
		BUFFER_SIZE,              // output buffer size 
		BUFFER_SIZE,              // input buffer size 
		NMPWAIT_USE_DEFAULT_WAIT, // client time-out 
		NULL);                    // default security attribute  




	if (INVALID_HANDLE_VALUE == hPipe)
	{
		printf("\nError occurred while creating the pipe: %d", GetLastError());
		system("Pause");
		return 1;  //Error
	}
	else
	{
		printf("\nCreateNamedPipe() was successful.");
	}

	printf("\nWaiting for client connection...");

	//Wait for the client to connect
	BOOL bClientConnected = ConnectNamedPipe(hPipe, NULL);

	if (FALSE == bClientConnected)
	{
		printf("\nError occurred while connecting to the client: %d", GetLastError());
		CloseHandle(hPipe);
		system("Pause");
		return 1;  //Error
	}
	else
	{
		printf("\nConnectNamedPipe() was successful.");
	}


	repeate();

}

```

#### Client Code    
```
#include "windows.h"
#include <iostream>
#include <tchar.h>
#include <stdio.h>


#define PipeName _T("\\\\.\\pipe\\testPipe")  //파이프의 이름 명시 


#define BUFFER_SIZE 1024 //1k
#define ACK_MESG_RECV "Message received successfully"

HANDLE hPipe;

int repeate() {
	char szBuffer[BUFFER_SIZE];

	printf("\nEnter a message to be sent to the server: ");
	std::cin.getline(szBuffer, BUFFER_SIZE);
	

	DWORD cbBytes;

	//Send the message to server
	BOOL bResult = WriteFile(
		hPipe,                // handle to pipe 
		szBuffer,             // buffer to write from 
		strlen(szBuffer) + 1,   // number of bytes to write, include the NULL
		&cbBytes,             // number of bytes written 
		NULL);                // not overlapped I/O 

	if ((!bResult) || (strlen(szBuffer) + 1 != cbBytes))
	{
		printf("\nError occurred while writing to the server: %d", GetLastError());
		CloseHandle(hPipe);
		system("Pause");
		return 1;  //Error
	}
	else
	{
		printf("\nWriteFile() was successful.");
	}

	repeate();

}

int main(int argc, char* argv[])
{
	//Connect to the server pipe using CreateFile()
	hPipe = CreateFile(
		PipeName,   // pipe name 
		GENERIC_READ |  // read and write access 
		GENERIC_WRITE,
		0,              // no sharing 
		NULL,           // default security attributes
		OPEN_EXISTING,  // opens existing pipe 
		0,              // default attributes 
		NULL);          // no template file 

	if (INVALID_HANDLE_VALUE == hPipe)
	{
		printf("\nError occurred while connecting to the server: %d", GetLastError());
		//One might want to check whether the server pipe is busy
		//This sample will error out if the server pipe is busy
		//Read on ERROR_PIPE_BUSY and WaitNamedPipe() for that
		system("Pause");
		return 1;  //Error
	}
	else
	{
		printf("\nCreateFile() was successful.");
	}

	repeate();
}

```



보다 자세한 내용은 다음 MSDN의 문서를 참조하면 좋을것 같습니다.   
https://docs.microsoft.com/ko-kr/windows/win32/ipc/pipes
