using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class MainMenu : MonoBehaviour
{
    public void NewGame()
    {
        SceneLoader.Load(SceneLoader.Scene.StartMap);
    }
    //public void Options()
    //{
    //    SceneLoader.Load(SceneLoader.Scene.Freeroam);
    //}
    public void QuitGame()
    {
        Application.Quit();
    }
}
