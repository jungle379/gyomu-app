import Head from "next/head";
import toast, { Toaster } from "react-hot-toast";

const notify = () => toast.error("ネットワークがつながっていません。");

const Home = () => {
  return (
    <>
      <Head>
        <title>toppage</title>
      </Head>
      <div className="text-4xl text-red-300">test</div>
      <div>
        <button className="" onClick={notify}>
          ネットワーク確認
        </button>
        <Toaster />
      </div>
    </>
  );
};

export default Home;
